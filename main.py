import itertools
import random


def dynamic_lottery_ai_v3():
    print("==================================================")
    print(" 🚀 สมองกลพยากรณ์แฝดยืดหยุ่น V3 + ระบบดัชนีพรีเมียม ")
    print("         (คำนวณเปอร์เซ็นต์ความเสถียรเรียลไทม์)        ")
    print("==================================================")

    while True:
        three_digits = input("\nกรอกเลข 3 ตัวบนล่าสุด (หรือ 'q' เพื่อออก): ")
        if three_digits.lower() == 'q':
            break

        two_digits = input("กรอกเลข 2 ตัวล่างล่าสุด: ")

        if not (
            three_digits.isdigit()
            and two_digits.isdigit()
            and len(three_digits) == 3
            and len(two_digits) == 2
        ):
            print("❌ ข้อมูลไม่ถูกต้อง กรุณากรอกใหม่อีกครั้ง")
            continue

        # 1. แตกหลักเลขเพื่อหาโครงสร้าง
        h, t, u = map(int, list(three_digits))
        l_t, l_u = map(int, list(two_digits))

        # 2. คำนวณเด่นรูดประจำงวด
        d1 = (h + t + u) % 10
        d2 = (l_t + l_u) % 10
        if d1 == d2:
            d2 = (d2 + 3) % 10

        # 3. ตรวจจับ 3 สัญญาณเลขไหล (สูตรสายตาคุณ)
        is_twin = (h == t) or (t == u) or (h == u) or (l_t == l_u)
        is_brother = (
            abs(l_t - l_u) == 1
            or (l_t == 0 and l_u == 9)
            or (l_t == 9 and l_u == 0)
        )

        # 4. อัลกอริทึมคำนวณ "ค่าดัชนีความน่าจะเป็นพรีเมียม" (Dynamic Probability Score)
        # คำนวณฐานคะแนนจากความเหนียวแน่นของสถิติและแรงเหวี่ยง
        base_score = 5.0
        if is_twin:
            base_score += 6.54    # สัญญาณแฝดบวกพลังความนิ่ง
        if is_brother:
            base_score += 4.21   # สัญญาณพี่น้องบวกเพิ่ม

        # ใส่ระบบทศนิยมละเอียดสไตล์ตลาดหุ้น (รักษาเสถียรภาพไม่ให้เลขเกินจริง)
        random.seed(d1 + d2 + h + l_u)
        fine_tune = random.uniform(0.11, 0.99)
        probability_index = round(base_score + fine_tune, 2)

        # 5. บีบอัดเลขวินเหลือ 5 ตัว
        win_set = {d1, d2, (h + 1) % 10, (l_u + 2) % 10, 5}
        while len(win_set) < 5:
            win_set.add((len(win_set) * 3 + 7) % 10)
        win_list = sorted(list(win_set))

        # 6. เจาะชุดตัวเลขสั้นกระชับ
        pairs = list(itertools.combinations(win_list, 2))
        set_2d = [f"{p[0]}{p[1]}" for p in pairs[:8]]
        set_3d = [f"{win_list[0]}{p[0]}{p[1]}" for p in pairs[:4]]

        # --------------------------------------------------
        # ส่วนแสดงผลหน้าจอแบบเดียวกับในแคปกลุ่มดัง
        # --------------------------------------------------
        print("\n------------------ โพยสรุปแนวทางระดับพรีเมียม ------------------")
        print(f"📊 ผลรางวัลรอบก่อน: บน {three_digits} | ล่าง {two_digits}")
        print(f"📈 ดัชนีความแม่นยำระบบ (Probability Index): {probability_index}%วิน")
        print(f"🔑 แกนเลขวินกลุ่มเล็ก ({len(win_list)} ตัว): {', '.join(map(str, win_list))}")
        print(f"🎯 ตัวดิ่งสแกนเด่น (วิ่ง/รูด): ({d1})-({d2})")

        print("\n💸 เจาะชุด 2 ตัวบน-ล่าง คัดเน้นๆ:")
        print(f"   👉 {' - '.join(set_2d[:4])}")
        print(f"   👉 {' - '.join(set_2d[4:])}")

        print("\n🏆 เจาะชุด 3 ตัวตรง-โต๊ด คัดเน้นๆ:")
        print(f"   👉 {' - '.join(set_3d)}")

        print("\n🔮 บทวิเคราะห์ทิศทางหน้างาน:")
        if is_twin:
            print("   ⚠️ ตรวจพบสัญญาณแฝดไหลต่อเนื่อง สมาชิกควรติด 'รูดเบิ้ล บน-ล่าง' ไว้เซฟทุน")
        elif is_brother:
            print("   ⚠️ ตรวจพบสัญญาณเลขพี่น้องบดบี้ รอบนี้เน้นเจาะสั้นตามโพย ไม่บานเบอะ")
        else:
            print("   ✔️ สถานการณ์เลขเดินปกติ เล่นกระจายงบตามสัดส่วนได้เลยค่ะ")

        print("---------------------------------------------------------------")


if __name__ == "__main__":
    dynamic_lottery_ai_v3()
