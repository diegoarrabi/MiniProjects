FasdUAS 1.101.10   ��   ��    k             l     ��  ��     !/usr/bin/osascript     � 	 	 & ! / u s r / b i n / o s a s c r i p t   
  
 l     ��������  ��  ��        i         I     �� ��
�� .aevtoappnull  �   � ****  J      ����  ��    k     �       r         I     �������� $0 iscalendaractive isCalendarActive��  ��    o      ���� 0 calendar_active        l   ��������  ��  ��        r        4    �� 
�� 
psxf  m   
    �   � / U s e r s / d i e g o i b a r r a / D e v e l o p e r / 1 _ m y P r o j e c t s / M i n i P r o j e c t s / O u t l o o k C a l e n d a r U p d a t e / c o u n t  o      ���� 0 count_file_path         l   ��������  ��  ��      ! " ! l   �� # $��   #  Get Previous Count    $ � % % $ G e t   P r e v i o u s   C o u n t "  & ' & r     ( ) ( n     * + * 4    �� ,
�� 
cpar , m    ����  + l    -���� - I   �� .��
�� .rdwrread****        **** . o    ���� 0 count_file_path  ��  ��  ��   ) o      ���� 0 previous_count   '  / 0 / I   !�� 1��
�� .ascrcmnt****      � **** 1 b     2 3 2 m     4 4 � 5 5   P r e v i o u s   C o u n t :   3 o    ���� 0 previous_count  ��   0  6 7 6 l  " "��������  ��  ��   7  8 9 8 l  " "�� : ;��   :  Get Current Count	    ; � < < $ G e t   C u r r e n t   C o u n t 	 9  = > = O  " 7 ? @ ? r   & 6 A B A c   & 2 C D C l  & 0 E���� E I  & 0�� F��
�� .corecnte****       **** F n   & , G H G 2  * ,��
�� 
wrev H 4   & *�� I
�� 
wres I m   ( ) J J � K K  C a l e n d a r��  ��  ��   D m   0 1��
�� 
TEXT B o      ���� 0 current_count   @ m   " # L L�                                                                                  wrbt  alis    8  Macintosh HD               �_JBD ����Calendar.app                                                   �����_J        ����  
 cu             Applications  #/:System:Applications:Calendar.app/     C a l e n d a r . a p p    M a c i n t o s h   H D   System/Applications/Calendar.app  / ��   >  M N M I  8 C�� O��
�� .ascrcmnt****      � **** O b   8 ? P Q P m   8 ; R R � S S  C u r r e n t   C o u n t :   Q o   ; >���� 0 current_count  ��   N  T U T l  D D��������  ��  ��   U  V W V l  D D�� X Y��   X &  Check if they are the same value    Y � Z Z @ C h e c k   i f   t h e y   a r e   t h e   s a m e   v a l u e W  [ \ [ Z   D x ] ^���� ] >  D I _ ` _ o   D E���� 0 previous_count   ` o   E H���� 0 current_count   ^ k   L t a a  b c b I   L U�� d���� 0 writetofile writeToFile d  e f e o   M P���� 0 current_count   f  g�� g o   P Q���� 0 count_file_path  ��  ��   c  h i h O  V i j k j I  \ h�� l��
�� .srctrun null���     srct l 4   \ d�� m
�� 
srct m m   ` c n n � o o . O u t l o o k   E v e n t s   T r a n s f e r��   k m   V Y p p�                                                                                      @ alis    <  Macintosh HD               �_JBD ����Shortcuts.app                                                  �����_J        ����  
 cu             Applications  $/:System:Applications:Shortcuts.app/    S h o r t c u t s . a p p    M a c i n t o s h   H D  !System/Applications/Shortcuts.app   / ��   i  q�� q L   j t r r b   j s s t s m   j m u u � v v  U p d a t e d :   t I   m r�������� 0 getdate getDate��  ��  ��  ��  ��   \  w x w l  y y��������  ��  ��   x  y�� y Z   y � z {���� z H   y { | | o   y z���� 0 calendar_active   { O  ~ � } ~ } I  � �������
�� .aevtquitnull��� ��� null��  ��   ~ m   ~   �                                                                                  wrbt  alis    8  Macintosh HD               �_JBD ����Calendar.app                                                   �����_J        ����  
 cu             Applications  #/:System:Applications:Calendar.app/     C a l e n d a r . a p p    M a c i n t o s h   H D   System/Applications/Calendar.app  / ��  ��  ��  ��     � � � l     ��������  ��  ��   �  � � � i     � � � I      �� ����� 0 writetofile writeToFile �  � � � o      ���� 0 	this_data   �  ��� � o      ���� 0 target_file  ��  ��   � l    G � � � � Q     G � � � � k    ( � �  � � � r     � � � c     � � � l    ����� � o    ���� 0 target_file  ��  ��   � m    ��
�� 
ctxt � l      ����� � o      ���� 0 target_file  ��  ��   �  � � � r   	  � � � I  	 �� � �
�� .rdwropenshor       file � 4   	 �� �
�� 
file � o    ���� 0 target_file   � �� ���
�� 
perm � m    ��
�� boovtrue��   � l      ����� � o      ���� 0 open_target_file  ��  ��   �  � � � I   �� � �
�� .rdwrwritnull���     **** � o    ���� 0 	this_data   � �� � �
�� 
refn � l    ����� � o    ���� 0 open_target_file  ��  ��   � �� ���
�� 
wrat � m    ����  ��   �  � � � I    %�� ���
�� .rdwrclosnull���     **** � l    ! ����� � o     !���� 0 open_target_file  ��  ��  ��   �  ��� � L   & ( � � m   & '��
�� boovtrue��   � R      ������
�� .ascrerr ****      � ****��  ��   � k   0 G � �  � � � Q   0 D � ��� � I  3 ;�� ���
�� .rdwrclosnull���     **** � 4   3 7�� �
�� 
file � o   5 6���� 0 target_file  ��   � R      ������
�� .ascrerr ****      � ****��  ��  ��   �  �� � L   E G � � m   E F�~
�~ boovfals�   � $  (string, file path as string)    � � � � <   ( s t r i n g ,   f i l e   p a t h   a s   s t r i n g ) �  � � � l     �}�|�{�}  �|  �{   �  � � � i     � � � I      �z�y�x�z 0 getdate getDate�y  �x   � k     P � �  � � � r     ! � � � l      ��w�v � I     �u�t�s
�u .misccurdldt    ��� null�t  �s  �w  �v   � K    
 � � �r � �
�r 
year � o    �q�q 0 y   � �p � �
�p 
mnth � o    �o�o 0 m   � �n ��m
�n 
day  � o    �l�l 0 d  �m   �  � � � l  " "�k � ��k   � , & pad the day and month if single digit    � � � � L   p a d   t h e   d a y   a n d   m o n t h   i f   s i n g l e   d i g i t �  � � � r   " 1 � � � n   " / � � � 7  % /�j � �
�j 
ctxt � m   ) +�i�i�� � m   , .�h�h�� � l  " % ��g�f � b   " % � � � m   " # � � � � �  0 0 � o   # $�e�e 0 d  �g  �f   � o      �d�d 0 day_str   �  � � � r   2 C � � � n   2 A � � � 7  7 A�c � �
�c 
ctxt � m   ; =�b�b�� � m   > @�a�a�� � l  2 7 ��`�_ � b   2 7 � � � m   2 3 � � � � �  0 0 � l  3 6 ��^�] � ]   3 6 � � � o   3 4�\�\ 0 m   � m   4 5�[�[ �^  �]  �`  �_   � o      �Z�Z 0 mon_str   �  � � � l  D D�Y � ��Y   � , & make ISO8601 date string without time    � � � � L   m a k e   I S O 8 6 0 1   d a t e   s t r i n g   w i t h o u t   t i m e �  � � � r   D M � � � c   D K � � � l  D I ��X�W � b   D I � � � b   D G � � � o   D E�V�V 0 mon_str   � m   E F � � � � �  - � o   G H�U�U 0 day_str  �X  �W   � m   I J�T
�T 
TEXT � o      �S�S 0 the_date   �  �R  L   N P o   N O�Q�Q 0 the_date  �R   �  l     �P�O�N�P  �O  �N   �M i     I      �L�K�J�L $0 iscalendaractive isCalendarActive�K  �J   k      	 r     

 m      �  C a l e n d a r o      �I�I 0 app_name  	 �H O    E     l   �G�F n     1    �E
�E 
pnam 2   �D
�D 
prcs�G  �F   o    �C�C 0 app_name   m    �                                                                                  sevs  alis    \  Macintosh HD               �_JBD ����System Events.app                                              �����_J        ����  
 cu             CoreServices  0/:System:Library:CoreServices:System Events.app/  $  S y s t e m   E v e n t s . a p p    M a c i n t o s h   H D  -System/Library/CoreServices/System Events.app   / ��  �H  �M       �B�B   �A�@�?�>
�A .aevtoappnull  �   � ****�@ 0 writetofile writeToFile�? 0 getdate getDate�> $0 iscalendaractive isCalendarActive �= �<�;�:
�= .aevtoappnull  �   � ****�<  �;     �9�8�7 �6�5�4�3 4�2 L�1 J�0�/�.�- R�, p�+ n�* u�)�(�9 $0 iscalendaractive isCalendarActive�8 0 calendar_active  
�7 
psxf�6 0 count_file_path  
�5 .rdwrread****        ****
�4 
cpar�3 0 previous_count  
�2 .ascrcmnt****      � ****
�1 
wres
�0 
wrev
�/ .corecnte****       ****
�. 
TEXT�- 0 current_count  �, 0 writetofile writeToFile
�+ 
srct
�* .srctrun null���     srct�) 0 getdate getDate
�( .aevtquitnull��� ��� null�: �*j+  E�O)��/E�O�j �k/E�O��%j 	O� *��/�-j �&E` UOa _ %j 	O�_  -*_ �l+ Oa  *a a /j UOa *j+ %Y hO� � *j UY h �' ��&�%�$�' 0 writetofile writeToFile�& �# �#    �"�!�" 0 	this_data  �! 0 target_file  �%   � ���  0 	this_data  � 0 target_file  � 0 open_target_file   �����������
� 
ctxt
� 
file
� 
perm
� .rdwropenshor       file
� 
refn
� 
wrat� 
� .rdwrwritnull���     ****
� .rdwrclosnull���     ****�  �  �$ H *��&E�O*�/�el E�O���j� O�j OeW X 	 
 *�/j W X 	 
hOf � ���!"�� 0 getdate getDate�  �  ! �����
�	� 0 y  � 0 m  � 0 d  � 0 day_str  �
 0 mon_str  �	 0 the_date  " ���������  ����� � ���
� 
Krtn
� 
year� 0 y  
� 
mnth� 0 m  
� 
day � 0 d  � 
�  .misccurdldt    ��� null
�� 
ctxt����
�� 
TEXT� Q*��������l E[�,E�Z[�,E�Z[�,E�ZO�%[�\[Zi\Z�2E�O�k %[�\[Zi\Z�2E�O��%�%�&E�O� ������#$���� $0 iscalendaractive isCalendarActive��  ��  # ���� 0 app_name  $ ����
�� 
prcs
�� 
pnam�� �E�O� 	*�-�,�U ascr  ��ޭ