########################################################
# Task A9_T7
# Developer Jussi Mäkelä
# Date 2025-12-03
########################################################

import sys
import os

def showHelp() -> None:
    # Display usage information.
    print("[USAGE] python A9_T7.py src_file dst_file")
    return None

def copyFile(PSrcFile: str, PDstFile: str) -> None:
    Proceed = False 
    
    # Check if destination file exists
    dst_path = PDstFile
    if os.path.exists(dst_path):
        print(f'Destination file "{PDstFile}" already exists.')
        response = input("Do you want to overwrite it? (y/n): ")
        if response.lower() == 'y':
            Proceed = True
        else:
            Proceed = False
    else:
        Proceed = True
    
    # Perform copy operation if proceed flag is set
    if Proceed:
        try:
            # Read from source file
            src_path = PSrcFile
            source_file = open(src_path, "r")
            content = ""
            while True:
                line = source_file.readline()
                if len(line) == 0:
                    break
                content += line
            source_file.close()
            
            # Write to destination file
            destination_file = open(dst_path, "w")
            destination_file.write(content)
            destination_file.close()
            
        except Exception as e:
            print(f'Couldn\'t copy "{PSrcFile}" to "{PDstFile}".')
            print(f"Error: {e}")
            print("Exiting program.")
            sys.exit(-1)
    
    return None

def main() -> None:
    print("Program starting.")
    
    # Check argument count
    if len(sys.argv) != 3:
        print("Invalid amount of arguments.")
        showHelp()
        print("Program ending.")
        return None
    
    # Get source and destination filenames from arguments
    SrcFile = sys.argv[1]
    DstFile = sys.argv[2]
    
    print(f'Source file "{SrcFile}"')
    print(f'Destination file "{DstFile}"')
    print(f'Copying file "{SrcFile}" to "{DstFile}".')
    
    copyFile(SrcFile, DstFile)
    
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
