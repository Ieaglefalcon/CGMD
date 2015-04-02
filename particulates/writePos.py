# position file for 1% particulate suspension 
import random

Lbox = 17.534
Np = 25
Ns =  4000
mol_s = 0
type_sol = 1
type_cen_p = 3
type_p = 2
DistBead = [-1, -1/3, 1/3, 1]

 # write position into file

fpos = open("coord.1per",'w')
fpos.write("# vol_p = 1%\n") 
fpos.write("%d atoms\n" %Ns) 
fpos.write("0 bonds\n")
fpos.write("0 angles\n")
fpos.write("0 dihedrals\n")
fpos.write("0 impropers\n")
fpos.write("\n")
fpos.write("3 atom types\n")
fpos.write("\n")
fpos.write("0 %f xlo xhi\n" %Lbox)
fpos.write("0 %f ylo yhi\n" %Lbox)
fpos.write("0 %f zlo zhi\n" %Lbox)
fpos.write("\n")
fpos.write("Masses\n")
fpos.write("\n")
fpos.write("1 1.0\n")
fpos.write("2 1.1\n")
fpos.write("3 1.1\n")
fpos.write("\n")
fpos.write("Atoms")
fpos.write("\n")
fpos.write("\n")

solPos =[]
cenPos = []
beadPos = []
 # positions for solvent particles
for i in range(Ns):
 	solPos[:] = [random.random()*Lbox,random.random()*Lbox,random.random()*Lbox]
 	fpos.write("%d %d %d %f %f %f\n" %(i+1, mol_s,type_sol,solPos[0],solPos[1],solPos[2]))

id = Ns

for j in range(Np):
	id = id + 1
	cenPos[:] = [random.random()*Lbox,random.random()*Lbox,random.random()*Lbox]
	fpos.write("%d %d %d %f %f %f\n" %(id, j+1, type_cen_p, cenPos[0], cenPos[1],cenPos[2]))

	for k in range(len(DistBead)):
		beadPos[:] = [cenPos[0], cenPos[1], cenPos[2]+DistBead[k]]
		id = id + 1
		fpos.write("%d %d %d %f %f %f\n" %(id, j+1,type_p, beadPos[0],beadPos[1],beadPos[2]))

fpos.close()








