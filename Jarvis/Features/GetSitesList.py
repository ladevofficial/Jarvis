def getSitesList():
    file = open('Features/Sites.txt', 'r')
    sites = []
    sites = file.readlines()
    nsites = []
    for site in sites:
        nsites.append(site.split())
    return nsites
    file.close()
