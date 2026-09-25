"""โปรแกรมสุ่มเลขสลากเพื่อความบันเทิง (2, 3 และ 6 หลัก)"""

from datetime import datetime
import random
import sys
import time


# ทำให้ข้อความไทยและเส้นกรอบ Unicode แสดงได้แม้ terminal ใช้ encoding เดิมของ Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


# ANSI colors: ใช้ได้กับ Windows Terminal และ terminal รุ่นใหม่ส่วนใหญ่
RESET = "\033[0m"
BOLD = "\033[1m"
GOLD = "\033[38;5;220m"
PURPLE = "\033[38;5;141m"
MINT = "\033[38;5;121m"
PINK = "\033[38;5;213m"
DIM = "\033[2m"


def clear_screen():
    """ล้างหน้าจอตามระบบปฏิบัติการ โดยไม่ต้องเรียกคำสั่งภายนอก"""
    print("\033[2J\033[H", end="")


def line(char="─"):
    print(f"{PURPLE}{char * 48}{RESET}")


def title():
    line("═")
    print(f"{BOLD}{GOLD}              ✦ LUCKY DRAW ✦{RESET}")
    print(f"{MINT}        สุ่มเลขสลากเพื่อความบันเทิง{RESET}")
    line("═")


def draw_number(digits):
    """สุ่มเลขโดยเก็บเลขศูนย์นำหน้าไว้ครบตามจำนวนหลัก"""
    return f"{random.randint(0, 10 ** digits - 1):0{digits}d}"


def spin_animation(digits, rounds=18, delay=0.06):
    """แสดงเลขจำลองวิ่งก่อนเผยผลจริงแบบสล็อตแมชชีน"""
    for turn in range(rounds):
        fake_number = "".join(random.choice("0123456789") for _ in range(digits))
        dots = "." * (turn % 4)
        message = f"{DIM}กำลังสุ่ม{dots:<3} {GOLD}{BOLD}{fake_number}{RESET}"
        sys.stdout.write("\r" + message + " " * 18)
        sys.stdout.flush()
        time.sleep(delay + turn * 0.004)

    sys.stdout.write("\r" + " " * 70 + "\r")
    sys.stdout.flush()


def show_result(digits, number):
    labels = {2: "เลขท้าย 2 ตัว", 3: "เลขท้าย 3 ตัว", 6: "รางวัลเลข 6 หลัก"}
    print()
    print(f"{GOLD}┌{'─' * 46}┐{RESET}")
    print(f"{GOLD}│{RESET}{BOLD}{labels[digits]:^46}{RESET}{GOLD}│{RESET}")
    print(f"{GOLD}│{' ' * 46}│{RESET}")
    print(f"{GOLD}│{RESET}{PINK}{BOLD}{number:^46}{RESET}{GOLD}│{RESET}")
    print(f"{GOLD}│{' ' * 46}│{RESET}")
    print(f"{GOLD}└{'─' * 46}┘{RESET}")
    print(f"{DIM}สุ่มเมื่อ {datetime.now():%d/%m/%Y %H:%M:%S}{RESET}\n")


def reveal_number(digits):
    """เล่น animation แล้วคืนผลรางวัลที่สุ่มได้"""
    print(f"\n{MINT}✦ เริ่มการสุ่มเลข {digits} หลัก{RESET}")
    spin_animation(digits)
    number = draw_number(digits)
    show_result(digits, number)
    return number


def show_history(history):
    if not history:
        print(f"\n{DIM}ยังไม่มีผลการสุ่มในรอบนี้{RESET}\n")
        return

    print(f"\n{BOLD}{MINT}ประวัติการสุ่มในรอบนี้{RESET}")
    line()
    for serial, (_, number, moment) in enumerate(history, start=1):
        print(f"  #{serial:<3}  {GOLD}{BOLD}{number}{RESET}  {DIM}{moment:%H:%M:%S}{RESET}")
    line()
    print()


def main():
    history = []

    while True:
        clear_screen()
        title()
        print("  [1] สุ่มเลข 2 หลัก")
        print("  [2] สุ่มเลข 3 หลัก")
        print("  [3] สุ่มเลข 6 หลัก")
        print("  [4] ✦ สุ่มครบทั้ง 2 / 3 / 6 หลัก")
        print("  [5] ดูประวัติการสุ่ม")
        print("  [0] ออกจากโปรแกรม")
        line()

        choice = input(f"{BOLD}เลือกเมนู:{RESET} ").strip()

        if choice in {"1", "2", "3"}:
            digits = {"1": 2, "2": 3, "3": 6}[choice]
            number = reveal_number(digits)
            history.append((digits, number, datetime.now()))
            input("กด Enter เพื่อกลับสู่เมนู...")
        elif choice == "4":
            print(f"\n{BOLD}{PINK}✦ ชุดรางวัล Lucky Draw ✦{RESET}")
            for digits in (2, 3, 6):
                number = reveal_number(digits)
                history.append((digits, number, datetime.now()))
                time.sleep(0.25)
            input("กด Enter เพื่อกลับสู่เมนู...")
        elif choice == "5":
            show_history(history)
            input("กด Enter เพื่อกลับสู่เมนู...")
        elif choice == "0":
            print(f"\n{MINT}ขอบคุณที่ใช้ Lucky Draw — ขอให้โชคดีครับ! ✨{RESET}\n")
            break
        else:
            print(f"\n{PINK}กรุณาเลือกเมนู 0 - 5 เท่านั้น{RESET}")
            input("กด Enter เพื่อลองใหม่...")


if __name__ == "__main__":
    main()
