def intro():
    print()
    print()
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░█████╗░███╗░░░███╗░█████╗░███████╗░█████╗░███╗░░██╗░██████╗░█████╗░██████╗░░█████╗░██████╗░██╗░░░██╗")
    print("██╔══██╗████╗░████║██╔══██╗╚════██║██╔══██╗████╗░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝")
    print("███████║██╔████╔██║███████║░░███╔═╝██║░░██║██╔██╗██║╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝░╚████╔╝░")
    print("██╔══██║██║╚██╔╝██║██╔══██║██╔══╝░░██║░░██║██║╚████║░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░░░╚██╔╝░░")
    print("██║░░██║██║░╚═╝░██║██║░░██║███████╗╚█████╔╝██║░╚███║██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░░░░██║░░░")
    print("╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚══╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░")
    print("by 𝔑𝔢𝔳𝔢𝔯𝔢𝔫𝔬𝔲𝔤𝔥")
    print()
    print('\033[93m' + '𝗗𝗶𝘀𝗰𝗹𝗮𝗺𝗲𝗿 : Any inappropriate use of this program is condemned and not welcomed'  + '\033[0m')
    print()
    print()
    search_value = input("𝗦𝗲𝗮𝗿𝗰𝗵 𝗣𝗿𝗼𝗱𝘂𝗰𝘁: ")
    print()
    print()
    return search_value

def region():
    region = input("Language: it, sp, ge, uk: ")
    match region:
        case "it":
            region = "https://www.amazon.it/"
        case "uk":
            region = "https://www.amazon.co.uk/"
        case "sp":
            region = "https://www.amazon.es/"
        case "ge":
            region = "https://www.amazon.ge/"
    return region