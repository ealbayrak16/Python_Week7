"""
Input : AABZA1111AEGTV5YH678MK4FM53B6
Output : MK4FM53B6
Input : AEGTV5VZ4PF94B6YH678
Output : VZ4PF94B6"""
import regex as re
text_ = "AEGTV5VZ4PF94B6YH678 AABZA1111AEGTV5YH678MK4FM53B6"
x = re.findall("[(A-Z)|(a-z)]{2}\d[(A-Z)|(a-z)]{2}\d{2}[(A-Z)|(a-z)]\d",text_)
print(" ".join(x))
