ch =raw_input();
if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
	if(ch=='A' or ch=='a' or ch=='E' or ch=='e' or ch=='I' or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
		print(ch,"Vowel")
	else:
		print(ch,"Consonant") 
else:
     print(ch,"invalid")
