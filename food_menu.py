food_menu = [
    {"1번 세트":["제육볶음","돈까스"]},
    {"2번 세트":["고등어구이", "불고기", "비빔밥"]},
    {"3번 세트":["샌드위치", "샐러드"]}
    ]
print("--- 도시락 메뉴 구성 ---")

for i in range(len(food_menu)):
    food_set_menu = food_menu[i]

    for j in food_set_menu:
        food_menu_in_menu = food_set_menu[j]

        for z in range(len(food_menu_in_menu)):
            setmenu_indi = food_menu_in_menu[z]

            print(f"세트 {i}의 메뉴 {z}번: {setmenu_indi}")

    print("----------------")
print("오늘의 메뉴 구성이 완료되었습니다.")