# mod-cli-demo-project

โปรเจกต์ตัวอย่างขนาดเล็ก ใช้ลองเล่น mod **task-status** และ **agent-router** ใน Claude CLI

ตัวโปรเจกต์เป็นโปรแกรมบันทึกรายจ่าย (Python, ไม่ต้องติดตั้งอะไรเพิ่ม) ที่ **ตั้งใจใส่บั๊กไว้ 1 จุด** และ **ยังขาดฟีเจอร์** ให้ Claude ทำ

```bash
python -m expenses.cli add food 120 --note "ข้าวมันไก่"
```
```bash
python -m expenses.cli report
```
```bash
python -m unittest
```

ตอนนี้เทสต์ล้ม 1 ตัว (`test_by_category_adds_up`) เพราะบั๊กใน `expenses/report.py`

## เริ่มลอง

```bash
cd C:\Users\CDT\dev\sandbox\mod-cli-demo-project
```
```bash
maverick
```

ในเซสชัน พิมพ์ `/router` เพื่อดูว่าโหลดการตั้งค่าจากไฟล์ไหน ต้องเห็น `Model settings from: /config + ...\.claude\agent-router.rules.json` (global) และไฟล์ของ project นี้

## prompt สำหรับลอง (ทีละข้อ)

| # | prompt | agent-router ควรจัดเป็น | ตัดสินโดย | task-status ควรแสดง |
|---|---|---|---|---|
| 1 | `แก้บั๊กให้เทสผ่าน` | `debugging` → none | rule (keyword `แก้บั๊ก`) | todo 2–4 ข้อ เช่น หาบั๊ก, แก้, รันเทสต์ |
| 2 | `by_category ใช้ที่ไหนบ้าง` | `codebase-search` → Explore | rule (keyword `ใช้ที่ไหนบ้าง`) | ไม่มี todo (งานขั้นตอนเดียว) |
| 3 | `วางแผนเพิ่มระบบงบประมาณรายเดือน แจ้งเตือนเมื่อใช้เกินงบ` | `planning` → Plan | rule (keyword `วางแผน`) | todo หลายข้อ |
| 4 | `เพิ่มคำสั่ง delete สำหรับลบรายการตาม index พร้อมเทสต์` | `implementation` | โมเดล (ไม่มี rule ตรง) | todo หลายข้อ |
| 5 | `เขียน docstring ภาษาไทยให้ทุกฟังก์ชันใน report.py` | `docs-writing` | โมเดล | todo 2–3 ข้อ |
| 6 | `รีวิวโค้ดใน cli.py หน่อย มีจุดไหนควรปรับ` | `code-review` | โมเดล | todo 2–3 ข้อ |

ข้อ 4–6 ตัดสินโดยโมเดล ผลอาจต่างจากตารางได้ ลองเช็กก่อนส่งได้ด้วย `/route <prompt>`

## ดูผล

- **แถบ `router ...` เหนือช่องพิมพ์:** ประเภท → agent, ความยาก, % ความมั่นใจ, แหล่งที่ตัดสิน (rule / llm / cache)
- **แถบ `Todo n/N`:** แผนงานของ task-status ขึ้นภายในไม่กี่วินาที
- **pane Task status:** เปิดด้วย `/todo`
- **toast `agent-router: <agent> runs on <model>`:** ขึ้นเมื่อ Claude เรียก subagent โดยไม่ระบุ model
- **`/router history`:** ประวัติการจัดประเภทของเซสชันนี้

## การตั้งค่าของ project นี้

[.claude/agent-router.rules.json](.claude/agent-router.rules.json)

- **rules:** keyword ภาษาไทยสำหรับ debugging, codebase-search, planning ตอบทันทีโดยไม่เรียกโมเดล
- **models:** ตั้งครบทุกค่า (tier, ทั้ง 11 ประเภท, agentModels, forceTier) จึงไม่ขึ้นกับไฟล์ global ต่างจาก global แค่ `docs-writing` → `wu/typhoon-thai`

แก้ไฟล์แล้วพิมพ์ `/router reload`
