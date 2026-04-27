# Phase 02: Auth Integration
Status: ⬜ Pending
Dependencies: Phase 01

## Objective
Tích hợp Supabase Auth vào giao diện người dùng, thay thế hệ thống login cũ.

## Requirements
- [ ] Thêm thư viện `@supabase/supabase-js` qua CDN.
- [ ] Cập nhật giao diện Đăng nhập: Thêm nút "Đăng nhập với Google".
- [ ] Code logic Đăng ký/Đăng nhập bằng Email/Password.
- [ ] Code logic Đăng nhập bằng Google (OAuth).
- [ ] Xử lý trạng thái Login (Persistence): Tự động nhận diện user khi quay lại trang.

## Implementation Steps
1. [ ] Cập nhật `index.html`: Thêm Supabase CDN script.
2. [ ] Sửa hàm `init()`: Thay đổi cách check user status sang Supabase.
3. [ ] Viết hàm `handleGoogleLogin()`.
4. [ ] Viết hàm `handleEmailLogin()` và `handleEmailSignUp()`.
5. [ ] Cập nhật UI Top Bar để hiển thị thông tin User từ Supabase.

## Test Criteria
- [ ] Đăng ký tài khoản mới thành công.
- [ ] Đăng nhập bằng Email thành công.
- [ ] Đăng nhập bằng Google (mở popup/redirect) thành công.
- [ ] Logout xóa sạch session.
