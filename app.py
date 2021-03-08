import os
import shutil


def move_file():
    desktop_path = r'C:\Users\mdsak\Desktop'
    for f in os.listdir(desktop_path):
        file_name , file_ext = os.path.splitext(f)
        try:
            if not file_ext:
                pass
            elif file_ext in ('.txt', '.doc','.docx', '.odt','.xlsx','.pptx','.pdf'):
                folder_path = r'C:\Users\mdsak\Desktop\Documents'
                old_file_name = file_name+file_ext
                isfile_exist = os.path.isfile(folder_path+'/'+old_file_name)
                if isfile_exist == True:
                    old_file = desktop_path+'/'+old_file_name
                    file_name = file_name+'a'
                    new_file = desktop_path+'/'+file_name+file_ext
                    file_rename = os.rename(old_file,new_file)
                else:
                    shutil.move(os.path.join(desktop_path,f'{file_name}{file_ext}'),
                                os.path.join(desktop_path,'Documents',f'{file_name}{file_ext}')
                                )
            elif file_ext in ('.jpg', '.png', '.JPG','.gif','.ico','.jpeg'):
                folder_path = r'C:\Users\mdsak\Desktop\Images'
                old_file_name = file_name+file_ext
                isfile_exist = os.path.isfile(folder_path+'/'+old_file_name)
                if isfile_exist == True:
                    old_file = desktop_path+'/'+old_file_name
                    file_name = file_name+'a'
                    new_file = desktop_path+'/'+file_name+file_ext
                    file_rename = os.rename(old_file,new_file)
                else:
                    shutil.move(os.path.join(desktop_path,f'{file_name}{file_ext}'),
                                os.path.join(desktop_path,'Images',f'{file_name}{file_ext}')
                                )
            elif file_ext in ('.zip','.z','.tar.gz','.rpm','.rar','.pkg','.deb','.7z','.arj'):
                folder_path = r'C:\Users\mdsak\Desktop\Compressed files'
                old_file_name = file_name+file_ext
                isfile_exist = os.path.isfile(folder_path+'/'+old_file_name)
                if isfile_exist == True:
                    old_file = desktop_path+'/'+old_file_name
                    file_name = file_name+'a'
                    new_file = desktop_path+'/'+file_name+file_ext
                    file_rename = os.rename(old_file,new_file)
                else:
                    shutil.move(os.path.join(desktop_path,f'{file_name}{file_ext}'),
                                os.path.join(desktop_path,'Compressed files',f'{file_name}{file_ext}')
                                )
            else:
                shutil.move(os.path.join(desktop_path, f'{file_name}{file_ext}'),
                            os.path.join(desktop_path, 'Others', f'{file_name}{file_ext}')
                            )

        except:
            pass

while True:
    move_file()