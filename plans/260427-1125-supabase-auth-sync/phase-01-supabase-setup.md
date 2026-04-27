# Phase 01: Supabase Setup
Status: ⬜ Pending
Dependencies: None

## Objective
Thiết lập dự án Supabase, cấu hình API keys và tạo cấu trúc Database (Schema).

## Implementation Steps
1. [ ] Khởi tạo dự án trên Supabase Dashboard.
2. [ ] Thiết lập Auth Providers: Bật Email (confirm email off để test nhanh) và Google Auth.
3. [ ] Tạo bảng `profiles`: Lưu thông tin người dùng bổ sung.
4. [ ] Tạo bảng `quiz_history`: Lưu kết quả các lần làm bài (tổng số câu đúng/sai, ngày làm).
5. [ ] Tạo bảng `wrong_answers`: Lưu chi tiết các câu làm sai để ôn tập.
6. [ ] Cấu hình RLS (Row Level Security): Đảm bảo user chỉ thấy dữ liệu của chính mình.

## Database Schema (SQL)
```sql
-- Quiz History Table
CREATE TABLE quiz_history (
  id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
  user_id uuid REFERENCES auth.users NOT NULL,
  category text,
  total_questions int,
  correct_count int,
  wrong_count int,
  score_percent int,
  created_at timestamp with time zone DEFAULT now()
);

-- Wrong Answers Table
CREATE TABLE wrong_answers (
  id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
  user_id uuid REFERENCES auth.users NOT NULL,
  question_id int NOT NULL,
  category text,
  created_at timestamp with time zone DEFAULT now()
);
```

## Output
- Dự án Supabase sẵn sàng.
- Bảng dữ liệu đã được tạo.
- API keys sẵn sàng để dán vào app.
