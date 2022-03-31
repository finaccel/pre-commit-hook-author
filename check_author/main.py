import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()
        
    errors         = []
    is_author      = False
    is_description = False
    for filename in args.filenames:
        count_lines = 0
        with open(filename, 'rb') as fb:  
            for line in fb:
                # check existing author
                if 'author' in line.decode():
                    is_author = True
                    
                # check existing description
                if 'description' in line.decode():
                    is_description = True
                
                if count_lines > 5:
                    break
                
                count_lines += 1
        
        # file is empty
        if count_lines <= 2:
            errors.append(TypeError(f"{filename} is empty"))
            continue
        
        if not is_author:
            errors.append(TypeError(f"{filename} has no author"))
            
        if not is_description:
            errors.append(TypeError(f"{filename} has no description (description to let others know the purpose of this file)"))
    
    if len(errors) > 0:
        return errors
    else:
        return 0

if __name__ == "__main__":
    main()