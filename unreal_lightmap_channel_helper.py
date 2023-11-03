#script by romasharf
#thanks to guys from Epic Games for the course in the description of this video https://youtu.be/Pxz8PAQR6_g?si=LfGMxryrHYkXWJ1E
#and for nice documentation https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/MeshBuildSettings.html?highlight=meshbuildsettings#unreal.MeshBuildSettings
#also many thanks to Gatis Kurzemnieks for his absolutely beautiful article https://www.rendereverything.com/unreal-minitip-batch-process-mesh-settings-with-python/

import unreal


#function finds "wrong" lightmap building settings for each lod of assets selected in content browser
def setNiceLightmapChannels():

    wrong_lm_settings_count = 0 #total amount of lightmap build settings to fix
    sm_edit_subsys = unreal.StaticMeshEditorSubsystem()
    EUL = unreal.EditorUtilityLibrary
    
    selectedAssets = EUL.get_selected_assets()
    print('***************************************')
    print('*** lightmap channels check started *** \n')
    print('***************************************')
    for selectedAsset in selectedAssets:
                
        lods_number = selectedAsset.get_num_lods() #number of lods in the asset

        #checking each lod in mesh asset
        number_of_lod = 0 #number of current lod to check
        for number_of_lod in range(lods_number):
            
            if (sm_edit_subsys.get_lod_build_settings(selectedAsset, number_of_lod).src_lightmap_index != 1) or (sm_edit_subsys.get_lod_build_settings(selectedAsset, number_of_lod).dst_lightmap_index != 1) or (sm_edit_subsys.get_lod_build_settings(selectedAsset, number_of_lod).generate_lightmap_u_vs == False):
                print('Wrong Lightmap build settings: '+str(selectedAsset))
                print('LOD: '+str(number_of_lod))
                print('Generate Lightmap UVs: '+str(sm_edit_subsys.get_lod_build_settings(selectedAsset, number_of_lod).generate_lightmap_u_vs))
                print("source lightmap channel: " + str(sm_edit_subsys.get_lod_build_settings(selectedAsset, number_of_lod).src_lightmap_index)) #get lod0 build settings
                print("destination lightmap channel: " + str(sm_edit_subsys.get_lod_build_settings(selectedAsset, number_of_lod).dst_lightmap_index)+'\n ') #get lod0 build settings
                print(' \n ')
                wrong_lm_settings_count = wrong_lm_settings_count + 1
            
    print('***************************************')        
    print('*** total amount of errors: ' + str(wrong_lm_settings_count) + ' ***')
    print('***************************************')
