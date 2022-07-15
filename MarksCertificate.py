sub1 = "Chemistry"
sub2 = "Physics"
sub3 = "Mathematics"
sub4 = "Islamic Studies"
sub5 = "Pakistan Studies"
sub1_T_M=100
sub2_T_M=100
sub3_T_M=100
sub4_T_M=50
sub5_T_M=50
sub1_o_M=90
sub2_o_M=90
sub3_o_M=95
sub4_o_M=45
sub5_o_M=40

Total_Marks = sub1_T_M + sub2_T_M + sub3_T_M + sub4_T_M + sub5_T_M 
Obtained_marks = sub1_o_M + sub2_o_M + sub3_o_M + sub4_o_M + sub5_o_M 


name = "Muhammad Tahir"
fname = "Muhammad Siddique"
rnumber = "171301"
college = "PIAIC"



print("\n\n\t\t********************** YOUR RESULT *********************\n\n")
print('\n\n\t\t***********Karachi Board Of Intermediate and Secondary Education*************\n\n')

print("\t\tCOLLEGE: ", college)
print("\n\t\tNAME:        ", name, "\t\tFATHER NAME: ", fname)
print("\n\n\t\tROLL NUMBER: ", rnumber)

print("\n\t\tSubject: ","\t\tTotal_Marks: ", "\t\tObtained_Marks: ")
print("\t\t", sub2, "\t\t", sub1_T_M ,"\t\t\t",  sub1_o_M)
print("\t\t", sub2, "\t\t", sub2_T_M ,"\t\t\t",  sub2_o_M)
print("\t\t", sub2, "\t\t", sub3_T_M ,"\t\t\t",  sub3_o_M)
print("\t\t", sub2, "\t\t", sub4_T_M ,"\t\t\t",  sub4_o_M)
print("\t\t", sub2, "\t\t", sub4_T_M ,"\t\t\t",  sub4_o_M)
print("\t\tTotal-Marks", "\t\t", Total_Marks ,"\t\t\t",  Obtained_marks)

if Obtained_marks >= 250:
    print("\n\t\Obtained MARKS: ", Obtained_marks, "\t\tRESULT: PASS")
else:
    print("\n\t\tTOTAL MARKS:", Obtained_marks, "\t\tRESULT: FAIL")