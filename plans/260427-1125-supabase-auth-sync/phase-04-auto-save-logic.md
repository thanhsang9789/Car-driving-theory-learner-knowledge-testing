# Phase 04: Auto-save Logic
Status: ⬜ Pending
Dependencies: Phase 03

## Objective
Thực hiện lưu trữ tự động khi người dùng rời khỏi trang hoặc không hoạt động.

## Requirements
- [ ] Theo dõi trạng thái hoạt động (Inactivity Timer - 10 phút).
- [ ] Theo dõi sự kiện đóng tab/trình duyệt (`visibilitychange`).
- [ ] Cơ chế Batch Update: Gom các câu sai trong phiên làm việc hiện tại để gửi 1 lần.

## Implementation Steps
1. [ ] Khai báo biến `sessionWrongAnswers` để lưu tạm trong memory.
2. [ ] Thiết lập `inactivityTimer`. Reset timer mỗi khi user click hoặc chọn đáp án.
3. [ ] Thêm event listener `visibilitychange`: Nếu `document.visibilityState === 'hidden'`, gọi hàm `persistPendingData()`.
4. [ ] Hàm `persistPendingData()`: Kiểm tra nếu có dữ liệu chưa lưu thì gửi lên Supabase.

## Test Criteria
- [ ] Đang làm dở, tắt trình duyệt, quay lại thấy câu sai đã được lưu vào Lịch sử.
- [ ] Treo máy 10 phút, kiểm tra database thấy dữ liệu đã được tự động cập nhật.
