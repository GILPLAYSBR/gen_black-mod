import blackwood


name= "C:\Users\gilbe\OneDrive\Documentos\LIVE FOR SPEED\CARROS\SAVEIRO GTI\data\veh"



s= blackwood.blk_file() 
s.load(name)
 

# me: sub objetos

for me in range(1,240):   
    s.set_mid(me)   
    ti = s.dump_mesh_as_string()
    open("F:\\LFS\\gen_black\\dist\\dump\\rim2_%i.obj"%(me),"w").write("".join(ti))
    print "MESH ", me, "DONE"

    
