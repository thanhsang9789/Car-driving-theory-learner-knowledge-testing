# Phase 03: Cloud Sync
Status: ⬜ Pending
Dependencies: Phase 02

## Objective
Chuyển đổi logic lưu trữ từ LocalStorage sang Supabase Database.

## Requirements
- [ ] Hàm `fetchHistory()`: Lấy dữ liệu từ bảng `quiz_history`.
- [ ] Hàm `saveQuizResult()`: Ghi kết quả bài thi vào Supabase.
- [ ] Hàm `syncWrongAnswers()`: Lưu danh sách câu sai vào bảng `wrong_answers`.

## Implementation Steps
1. [ ] Sửa logic trong hàm `renderHistory()` để gọi API Supabase.
2. [ ] Cập nhật màn hình Kết quả (Results Screen): Sau khi làm xong, thay vì lưu `localStorage`, gọi `supabase.from('quiz_history').insert(...)`.
3. [ ] Xử lý đồng bộ dữ liệu cũ: (Tùy chọn) Nếu có data trong LocalStorage, hỏi user có muốn up lên cloud không.

## Test Criteria
- [ ] Làm bài trên máy A, đăng nhập máy B thấy kết quả.
- [ ] Các câu làm sai được hiển thị đúng trong tab Lịch sử.
