
from book import book1
from book import book2
from book import book3
from book import shelf
from pizza import pizza1
from pizza import pizza2
from pizza import pizza3
from pizza import freezer
import numpy as np
import copy
from itertools import product

print("\n**********Start Mapping**********")


def comparenormals(a,b):
	value=1
	for i in range(3):
		if a[i]!=b[i]:
			value=0
	return value

def printresultofmapping(resultofmapping):
	for mapping in resultofmapping:
		print("\n\nhere is a mapping:")
		for surfacemappingrow in mapping:
			print("\nhere is a pair of surface mappings:")
			for surface in surfacemappingrow:
				print("here is a surface: "+str(surface))


def mapping(source, target):
	mappingnumber=1
	all24mappinglist = []
	box_mapping = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
	for firsttargetsurface in target.surfaces: # Loops through the 6 surfaces of target (pizza)
		remainingtargetsurfaces = target.surfaces[:] # List of all 6 surfaces
		print(remainingtargetsurfaces)
		remainingtargetsurfaces.remove(firsttargetsurface) # List of 5 remaining surfaces
		print("########################################################################")
		print(remainingtargetsurfaces)
		print("########################################################################")
		print(firsttargetsurface)
		print("########################################################################")
		box_mapping[0][0] = source.surfaces[0]
		box_mapping[0][1] = firsttargetsurface
		# Select an adjacent surface on source
		#this looks for the surface that shares edge[0] AND edge[1]
		for edge in source.edges:
			if (edge[0] in source.surfaces[0][0:4]) and (edge[1] in source.surfaces[0][0:4]):
				print("Edge in source edges is: ",edge)
				break
		for adjacent_candidate in source.surfaces[1:]:
			if (edge[0] in adjacent_candidate[0:4]) and (edge[1] in adjacent_candidate[0:4]):
				print("Adjacent source candidate surface is: ",adjacent_candidate)
				break
		box_mapping[1][0] = adjacent_candidate


		#now select adjacent candidates on target
		#find the target surface that is opposite (not adjacent)
		#and remove it
		oppositenormal=[-1*firsttargetsurface[4],-1*firsttargetsurface[5],-1*firsttargetsurface[6]]
		print("firsttargetsurface ")
		print(firsttargetsurface)
		print("the opposite normal")
		print(oppositenormal)
		for opposite_candidate in remainingtargetsurfaces: #to remove the opposite normal
			if (
				(opposite_candidate[4]==oppositenormal[0])
				and
				(opposite_candidate[5]==oppositenormal[1])
				and
				(opposite_candidate[6]==oppositenormal[2])
				):
				print("Removing opposite candidate!")
				remainingtargetsurfaces.remove(opposite_candidate)



		for adjacent_candidate in remainingtargetsurfaces:
			#adjacent_candidate goes through all 4 remaining surfaces
			#but only 4 are actually adjacent
			#now check is adjacent_candidate actually adjacent
			print("***************************************************************************")
			#print("\n")
			print("we are on mapping "+ str(mappingnumber))
			mappingnumber+=1
			#print("\n")
			print("**************************************************************************")


			box_mapping[1][1] = adjacent_candidate
	#***************************************************************************************************

			#now we're ready to step around the remaining 3 adjacent surfaces
			#here we make variables sa,sb... of the normals
			
			print("\nHere are the cross product results for source:")
			sa = np.array(box_mapping[0][0][4:7])
			#print(sa)  
			sb = np.array(box_mapping[1][0][4:7])
			#print(sb)
			sc = np.cross(sa,sb)
			print(sc)
			sd = np.cross(sa,sc)
			print(sd)
			se = np.cross(sa,sd)
			print(se)
			sf = np.cross(sc,sb)
			print(sf)
			for s in source.surfaces:
				if comparenormals( s[4:7] , sc):
					break
			box_mapping[2][0] = s

			for s in source.surfaces:
				if comparenormals( s[4:7] , sd):
					break
			box_mapping[3][0] = s

			for s in source.surfaces:
				if comparenormals( s[4:7] , se):
					break
			box_mapping[4][0] = s
		
			for s in source.surfaces:
				if comparenormals( s[4:7] , sf):
					break
			box_mapping[5][0] = s

			print("\nHere are the cross product results for the target:")
			ta = np.array(box_mapping[0][1][4:7])
			#print(ta)  
			tb = np.array(box_mapping[1][1][4:7])
			#print(tb)
			tc = np.cross(ta,tb)
			print(tc)
			td = np.cross(ta,tc)
			print(td)
			te = np.cross(ta,td)
			print(te)
			tf = np.cross(tc,tb)
			print(tf)
			for t in target.surfaces:
				if comparenormals( t[4:7] , tc):
					break
			box_mapping[2][1] = t

			for t in target.surfaces:
				if comparenormals( t[4:7] , td):
					break
			box_mapping[3][1] = t

			for t in target.surfaces:
				if comparenormals( t[4:7] , te):
					break
			box_mapping[4][1] = t
		
			for t in target.surfaces:
				if comparenormals( t[4:7] , tf):
					break
			box_mapping[5][1] = t

			

			"""
			# Here we look at assigining the aspect ratio to each surface, and determining similarity
			ratio = []
			for area in surfaces:
				j = len(surfaces[0:1])/len(surfaces[1:2])
				k = len(surfaces[1:2])/len(surfaces[0:1])
				m = min(j,k)
				print(m)
				ratio.append(surfaces[9])
				if m.source  m.target:
					ratioscore = 1.0
				else:
					ratioscore = -1.0
			"""


			print("\nHere is a candidate mapping")
			print(box_mapping[1][1])			

			all24mappinglist.append(copy.deepcopy(box_mapping))

			#print("\nHere is a complete list of 24 mappings:")
			#print(all24mappinglist)
	#print(all24mappinglist)
	printresultofmapping(all24mappinglist)
	return all24mappinglist


resultofmapping=mapping(book1,pizza2)

#printresultofmapping(resultofmapping)

def scoringf(all24mappings):
	# Here we look at assigining a score for each similar surface property
	mappingcount=1
	for mapping in all24mappings:
		print("now doing mapping "+str(mappingcount))
		mappingcount+=1
		scoring = []
		print("hello")
		#print(mapping)
		for innermapping in mapping:
			if (innermapping[0][7] == "") or  (innermapping[1][7]=="") :
				mappingscore = 0.5
			elif innermapping[0][7] == innermapping[1][7] :
				mappingscore = 1.0
			else:
				mappingscore = 0.1
			scoring.append(mappingscore)
		totalscore = sum(scoring)
		print(scoring)
		print(totalscore)
		#print("\n")

scoringf(resultofmapping)

#box_mapping=resultofmapping[0]

#for mappingscore in box_mapping[0]: # Source wall surface
#	print(mappingscore)




"""
compute the score for 1 particular mapping

look at each pair of surfaces that are mapped

go through surface properties list, and where they are similar give a bonus, and where they are different give a penalty

the full score of one mapping is the sum of the surface scores (aspect ratio + properties)
"""