# Stable Diffusion Exe
# Python 3
# Execute stable diffusion .bat file

import subprocess
import os

print('#-------------------------------------------#')
print('# Stable Diffusion Quick Exe by SpawnTerror #')
print('#-------------------------------------------#')
print(f' ')
current_dir = os.getcwd()
print(f'Detecting current dir = ', current_dir)

file_name = "webui-user.bat"
file_path = current_dir + '\\' + file_name
print(f'Generating the filepath = ', file_path)
print(f' ')

if os.path.exists(file_path):
    print(f'#-----------------------------------#')
    print(f'# Executing the webui-user.bat file #')
    print(f'#-----------------------------------#')
    print(f' ')
    os.chdir(current_dir)
    subprocess.call(file_path, shell=True)
else:
    print(f'This exe has to be located within your \'stable-diffusion-webui\' folder!')
    input(f'Press any key to exit...')

