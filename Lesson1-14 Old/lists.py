def playWithLists():
    univs = []
    techs = ['MIT','Cal Tech']
    ivys = ['Harvard','Yale','Brown']
    print('univs:')
    print(univs)
    print('techs')
    print(techs)
    print('ivys')
    print(ivys)
    input()
    univs.append(techs)
    print('append techs to univs:')
    print(univs)
    input()
    print('append yvis to techs')
    techs.append(ivys)
    print('techs:')
    print(techs)
    print('univs:')
    print(univs)
    input()
    techs.remove(ivys)
    print('remove ivys from techs')
    print('techs:')
    print(techs)
    print('univs:')
    print(univs)
    input()
    for univ in univs:
        print(univ)
        for elem in univ:
            print(elem)
    univs = techs + ivys
    print('univs')
    print(univs)
    print('append ivys')
    univs.append(ivys)
    print(univs)
    print('univs[-1][0]')
    print(univs[-1][0])
    print('univs[-1][-1]')
    print(univs[-1][-1])
    print('univs[-1][-1][0]')
    print(univs[-1][-1][0])