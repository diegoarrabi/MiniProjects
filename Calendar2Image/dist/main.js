import nodeHtmlToImage from 'node-html-to-image';
import font2base64 from 'node-font2base64';
import fs from 'fs';
import os from 'os';
import path from 'path';
function expandTilde(filePath) {
    if (filePath.startsWith('~/')) {
        return path.join(os.homedir(), filePath.slice(2));
    }
}
const _data = font2base64.encodeToDataUrlSync(path.resolve(import.meta.dirname, '../src/resources/SF-Pro.ttf'));
const htmlDoc = fs.readFileSync(path.resolve(import.meta.dirname, '../src/calendar.html'), 'utf-8');
const bodyContent = htmlDoc.match(/<body[^>]*>([\s\S]*?)<\/body>/i)?.[1] || '';
const styleContent = htmlDoc.match(/<style[^>]*>([\s\S]*?)<\/style>/i)?.[1] || '';
const htmlStr = `
<html>
    <head>
        <style>
            @font-face {
                font-family: 'SF Pro';
                src: url("{{{_data}}}") format('woff2'); // don't forget the format!
            }
            ${styleContent}
        </style>
    </head>
        <body>
            ${bodyContent}
        </body>
    </html>
`;
nodeHtmlToImage({
    output: path.join(os.homedir(), 'Downloads', 'calendar.png'),
    html: htmlStr,
    content: { _data: _data },
    transparent: true,
    quality: 100
}).then(() => console.log('image successfully created'));
