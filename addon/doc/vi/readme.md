# Tài liệu hướng dẫn Vision Assistant Pro

**Vision Assistant Pro** là trợ lý AI đa phương thức tiên tiến dành cho NVDA. Nó tận dụng các mô hình Gemini của Google để cung cấp khả năng đọc, dịch, đọc chính tả bằng giọng nói và phân tích tài liệu thông minh trên màn hình.

_Tiện ích bổ sung này được phát hành ra cộng đồng để vinh danh Ngày Quốc tế Người khuyết tật._

## 1. Cài đặt & Cấu hình

đi đến **NVDA Trình đơn > Tùy Chọn > Cài Đặt > Vision Assistant Pro**.

- **API Key:** Yêu cầu. Nhận khóa miễn phí từ [Google AI Studio](https://aistudio.google.com/).
- **Mô hình:** Chọn giữa các mẫu **Flash** (Nhanh nhất/Miễn phí) hoặc **Pro** (Thông minh cao) dựa trên nhu cầu của bạn.
- **Proxy URL:** Không bắt buộc. Sử dụng điều này nếu Google bị chặn trong khu vực của bạn. Bạn cần một địa chỉ máy chủ (URL) nhận yêu cầu của bạn và chuyển tiếp chúng đến API Gemini.
- **Công cụ OCR:** Chọn giữa **Chrome (nhanh)** để có kết quả nhanh hoặc **Gemini (đã định dạng)** để bảo toàn bố cục và nhận dạng bảng tốt hơn.
- **Giọng TTs:** Chọn kiểu giọng nói ưa thích để tạo file âm thanh từ các trang tài liệu.
- **Chuyển đổi thông minh:** Tự động hoán đổi ngôn ngữ nếu văn bản nguồn khớp với ngôn ngữ đích.
- **Đầu ra trực tiếp:** Bỏ qua cửa sổ trò chuyện và thông báo phản hồi trực tiếp qua lời nói.
- **Tích hợp bộ nhớ tạm:** Tự động sao chép phản hồi AI vào bộ nhớ tạm.

## 2. Lớp lệnh và phím tắt

Để tránh xung đột bàn phím, tiện ích bổ sung này sử dụng **Lớp lệnh**.

1. Nhấn **NVDA + Shift + V** (Master Key) để kích hoạt lớp (bạn sẽ nghe thấy tiếng bíp).
2. Nhả phím, sau đó nhấn một trong các phím đơn sau:

| phím tắt                    | chức năng             | mô tả                                                                 |
|-----------------------------|----------------------|-----------------------------------------------------------------------------|
| **T**           | trình dịch thông minh     | Dịch văn bản dưới con trỏ điều hướng. Ưu tiên lựa chọn.      |
| **Shift + T**           | Dịch từ bộ nhớ | dịch nội dng trong bộ nhớ. **khuyên dùng cho trình duyệt web**.            |
| **S**           | Đọc chính tả thông minh       | Chuyển đổi lời nói thành văn bản. Nhấn một lần để bắt đầu, một lần nữa để dừng và gõ.       |
| **R**           | Tinh chỉnh văn bản         | Tóm tắt, sửa lỗi ngữ pháp, giải thích hoặc chạy **Prompts Tùy chỉnh**.                 |
| **C**           | Giải CAPTCHA        | Tự động chụp và giải CAPTCHA.                                 |
| **V**           | hỗ trợ nhìn đối tượng        | Mô tả đối tượng điều hướng với cuộc trò chuyện tiếp theo.                         |
| **O**           | hỗ trợ nhìn toàn màn hình    | Phân tích toàn bộ bố cục và nội dung màn hình.                                  |
| **Shift + V** | Phân tích video trực tuyến | Phân tích video **YouTube** hoặc **Instagram** qua URL.                        |
| **D**           | Trình đọc tài liệu | Trình đọc nâng cao cho PDF và hình ảnh với lựa chọn phạm vi trang.               |
| **F**           | File OCR             | OCR trực tiếp từ image/PDF file.                                             |
| **A**           |Phiên âm âm thanh    | phiên âm MP3/WAV/OGG files.                                               |
| **L**         | Báo cáo trạng thái | Thông báo trạng thái hiện tại (ví dụ: "Đang tải lên...", "Không hoạt động").                |
| **U**           | kiểm tra cập nhật         | Kiểm tra GitHub cho phiên bản mới nhất.                                            |
| **H** | Lệnh trợ giúp | Hiển thị danh sách đầy đủ tất cả các phím tắt có sẵn và mô tả của chúng trong lớp lệnh. |

### 2.1 Phím tắt trình đọc tài liệu (Trình xem bên trong)
Khi một tài liệu được mở thông qua lệnh **D** :
- **Ctrl + PageDown:** Chuyển sang trang tiếp theo (thông báo số trang).
- **Ctrl + PageUp:** Chuyển về trang trước (thông báo số trang).
- **Alt + A:** Mở hộp thoại trò chuyện để đặt câu hỏi về tài liệu.
- **Alt + R:** Buộc quét lại trang hiện tại hoặc tất cả các trang bằng công cụ Gemini.
- **Alt + G:** Tạo và lưu file âm thanh chất lượng cao (WAV) từ nội dung.
- **Alt + S / Ctrl + S:** Lưu văn bản được trích xuất dưới dạng tệp TXT hoặc HTML.

## 3. tùy chỉnh Prompts & biến

tạo lệnh trong cài đặt: `Name:Prompt Text` (tách biệt với `|` hoặc dòng mới).

### Biến có sẵn

| biến         | Mô tả                                      | Nhập đầu vào       |
|------------------|--------------------------------------------------|------------------|
| `[selection]`    | Currently selected text                          | Text             |
| `[clipboard]`    | Clipboard content                                | Text             |
| `[screen_obj]`   | Screenshot of navigator object                   | Image            |
| `[screen_full]`  | Full screen screenshot                           | Image            |
| `[file_ocr]`     | Select image/PDF/TIFF (defaults to "Extract text")| Image, PDF, TIFF |
| `[file_read]`    | Select text document                             | TXT, Code, PDF   |
| `[file_audio]`   | Select audio file                                | MP3, WAV, OGG    |

### Ví dụ Prompts tùy chỉnh

- **Quick OCR:** `My OCR:[file_ocr]`
- **Translate Image:** `Translate Img:Extract text from this image and translate to Persian. [file_ocr]`
- **Analyze Audio:** `Summarize Audio:Listen to this recording and summarize the main points. [file_audio]`
- **Code Debugger:** `Debug:Find bugs in this code and explain them: [selection]`

***
**Lưu ý:** Cần có kết nối internet hoạt động cho tất cả các tính năng AI. TIFF nhiều trang được xử lý tự động.

## Thay đổi cho 4.0

*   **Trình đọc tài liệu nâng cao:** Trình xem PDF và hình ảnh mới mạnh mẽ với tính năng chọn phạm vi trang, xử lý nền và điều hướng `Ctrl+PageUp/Down` liền mạch.
*   **Trình đơn con mới:** Đã thêm menu con "Vision Assistant" trong menu Công cụ của NVDA để truy cập nhanh hơn vào các tính năng, cài đặt và tài liệu.
*   **Tùy chỉnh linh hoạt:** Giờ đây, bạn có thể chọn công cụ OCR và giọng nói TTS ưa thích của mình trực tiếp từ bảng cài đặt.
*   **Hỗ trợ nhiều khóa API:** Đã thêm hỗ trợ cho nhiều khóa API Gemini để đảm bảo dịch vụ liên tục. Bạn có thể nhập một khóa trên mỗi dòng hoặc phân tách chúng bằng dấu phẩy trong cài đặt.
*   **Công cụ OCR thay thế:** Đã giới thiệu công cụ OCR mới để đảm bảo khả năng nhận dạng văn bản đáng tin cậy ngay cả khi đạt đến giới hạn API Gemini.
*   **Xoay khóa API thông minh:** Tự động chuyển sang và ghi nhớ khóa API hoạt động nhanh nhất để vượt qua giới hạn mà không cần can thiệp thủ công.
*   **Chuyển tài liệu sang âm thanh:** Khả năng tích hợp để tạo và lưu các file âm thanh chất lượng cao (WAV) từ các trang tài liệu trực tiếp trong trình đọc.
*   **Hộp thoại Cập nhật được thiết kế lại:** giao diện mới có thể truy cập với hộp văn bản để đọc rõ ràng các thay đổi của phiên bản trước khi cài đặt.
*   **Trạng thái hợp nhất & UX:** Hộp thoại file được tiêu chuẩn hóa trên tiện ích bổ sung và nâng cao lệnh 'L' để báo cáo tiến trình theo thời gian thực cho tất cả các tác vụ nền.

## thay đổi cho 3.6.0

*   **Hệ thống trợ giúp:** Đã thêm lệnh trợ giúp (`H`) trong Lớp lệnh để cung cấp danh sách dễ truy cập gồm tất cả các phím tắt và chức năng của chúng.
*   **Phân tích video trực tuyến:** Hỗ trợ mở rộng để bao gồm các video **Twitter (X)**. Đồng thời cải thiện khả năng phát hiện và độ ổn định của URL để có trải nghiệm đáng tin cậy hơn.
*   **Đóng góp cho dự án:** Đã thêm tùy chọn  quyên góp hộp thoại cho những người dùng muốn hỗ trợ các bản cập nhật trong tương lai và sự phát triển liên tục của dự án.

## Thay đổi cho 3.5.0

*   **Lớp lệnh:** Giới thiệu hệ thống Lớp Lệnh (mặc định: `NVDA+Shift+V`) để nhóm các phím tắt dưới một phím chính duy nhất. Ví dụ, thay vì nhấn `NVDA+Control+Shift+T` để dịch, bây giờ bạn nhấn `NVDA+Shift+V` theo sau là `T`.
*   **Phân tích video trực tuyến:** Đã thêm một tính năng mới để phân tích video YouTube và Instagram trực tiếp bằng cách cung cấp URL.

## Thay đổi cho 3.1.0

*   **Chế độ đầu ra trực tiếp:** Đã thêm tùy chọn bỏ qua hộp thoại trò chuyện và nghe phản hồi AI trực tiếp qua giọng nói để có trải nghiệm nhanh hơn và liền mạch hơn.
*   **Tích hợp bộ nhớ tạm:** Đã thêm cài đặt mới để tự động sao chép phản hồi AI vào bảng nhớ tạm.

## THAY ĐỔI CHO 3.0

*   **NGÔN NGỮ MỚI:** đã thêm bản dịch  **Persian** VÀ **Vietnamese** 
*   **Mô hình AI mở rộng:Sắp xếp lại danh sách lựa chọn model với các tiền tố rõ ràng (`[Free]`, `[Pro]`, `[Auto]`) để giúp người dùng phân biệt giữa model miễn phí và model có giới hạn (trả phí). Đã thêm hỗ trợ cho **Gemini 3.0 Pro** and **Gemini 2.0 Flash Lite**.
*   **tính ổn định của đọc chính tả thông minh:** Cải thiện đáng kể độ ổn định của Đọc chính tả thông minh. Đã thêm tính năng kiểm tra an toàn để bỏ qua các đoạn âm thanh ngắn hơn 1 giây, ngăn ngừa ảo giác AI và lỗi trống.
*   **sử lí File:** Đã khắc phục sự cố tải lên tệp có tên không phải tiếng Anh không thành công.
*   **tối ưu hóa Prompt:** Cải thiện logic dịch và kết quả hỗ trợ nhìn có cấu trúc.

## Thay đổi cho phiên bản 2.9

*   **Đã thêm bản dịch tiếng Pháp và tiếng Thổ Nhĩ Kỳ.**
*   **Chế độ xem định dạng:** Đã thêm nút "Xem định dạng" trong hộp thoại trò chuyện để xem cuộc trò chuyện có định dạng phù hợp (tiêu đề, định dạng, mã) trong cửa sổ có thể duyệt tiêu chuẩn.
*   **Cài đặt Markdown:** Đã thêm tùy chọn mới "Làm sạch makdownr trong trò chuyện" trong Cài đặt. Việc bỏ chọn tùy chọn này sẽ cho phép người dùng xem cú pháp Markdown thô (ví dụ: `**`, `#`) trong cửa sổ trò chuyện.
*   **Quản lý hộp thoại:** Đã khắc phục sự cố trong đó "Tinh chỉnh văn bản" hoặc cửa sổ trò chuyện mở nhiều lần hoặc không lấy nét chính xác.
*   **Cải tiến UX:** Tiêu đề hộp thoại tệp được tiêu chuẩn hóa thành "Mở" và loại bỏ các thông báo bằng giọng nói dư thừa (ví dụ: "Mở menu...") để có trải nghiệm mượt mà hơn.

## Thay đổi cho 2.8

* Đã thêm bản dịch tiếng Ý.
*   **Báo cáo trạng thái:** Đã thêm lệnh mới (NVDA+Control+Shift+I) để thông báo trạng thái hiện tại của tiện ích bổ sung (ví dụ: "Đang tải lên...", "Phân tích...").
*   **Xuất HTML:** Nút "Lưu nội dung" trong hộp thoại kết quả hiện lưu kết quả đầu ra dưới dạng tệp HTML được định dạng, giữ nguyên các kiểu như tiêu đề và văn bản in đậm.
*   **Giao diện người dùng cài đặt:** Cải thiện bố cục bảng Cài đặt với khả năng phân nhóm có thể truy cập được.
*   **Mẫu mới:** Đã thêm hỗ trợ cho gemini-flash-mới nhất và gemini-flash-lite-mới nhất.
*   **Ngôn ngữ:** Đã thêm tiếng Nepal vào các ngôn ngữ được hỗ trợ.
*   **Tinh chỉnh logic menu:** Đã sửa lỗi nghiêm trọng khiến lệnh "Tinh chỉnh văn bản" không thành công nếu ngôn ngữ giao diện NVDA không phải là tiếng Anh.
*   **Đọc chính tả:** Cải thiện tính năng phát hiện khoảng lặng để ngăn văn bản xuất ra không chính xác khi không có giọng nói nào được nhập vào.
*   **Cài đặt cập nhật:** "Kiểm tra các bản cập nhật khi khởi động" hiện bị tắt theo mặc định để tuân thủ các chính sách của Cửa hàng tiện ích bổ sung.
* Dọn dẹp mã.

## Thay đổi cho 2.7

* Đã di chuyển cấu trúc dự án sang Mẫu tiện ích bổ sung NV Access chính thức để tuân thủ các tiêu chuẩn tốt hơn.
* Triển khai logic thử lại tự động đối với các lỗi HTTP 429 (Giới hạn tốc độ) để đảm bảo độ tin cậy khi lưu lượng truy cập cao.
* Lời nhắc dịch được tối ưu hóa để có độ chính xác cao hơn và xử lý logic "Hoán đổi thông minh" tốt hơn.
* Cập nhật bản dịch tiếng Nga.

## Thay đổi cho 2.6

* Đã thêm hỗ trợ dịch tiếng Nga (Cảm ơn nvda-ru).
* Đã cập nhật thông báo lỗi để cung cấp phản hồi mang tính mô tả hơn về khả năng kết nối.
* Đã thay đổi ngôn ngữ mục tiêu mặc định sang tiếng Anh.

## Thay đổi cho 2.5

* Đã thêm Lệnh OCR tệp gốc (NVDA+Control+Shift+F).
* Đã thêm nút "Lưu trò chuyện" vào hộp thoại kết quả.
* Đã triển khai hỗ trợ bản địa hóa đầy đủ (i18n).
* Chuyển phản hồi âm thanh sang mô-đun âm gốc của NVDA.
* Đã chuyển sang API tệp Gemini để xử lý tốt hơn các tệp PDF và âm thanh.
* Đã sửa lỗi sự cố khi dịch văn bản có dấu ngoặc nhọn.

## Thay đổi cho 2.1.1

* Đã khắc phục sự cố trong đó biến [file ocr] không hoạt động chính xác trong Lời nhắc Tùy chỉnh.

## Thay đổi cho 2.1

* Chuẩn hóa tất cả các phím tắt để sử dụng NVDA+Control+Shift nhằm loại bỏ xung đột với bố cục Laptop của NVDA và các phím nóng hệ thống.

## Thay đổi cho 2.0

* Triển khai hệ thống Tự động cập nhật tích hợp.
* Đã thêm Bộ đệm dịch thuật thông minh để truy xuất ngay văn bản đã dịch trước đó.
* Đã thêm Bộ nhớ hội thoại để tinh chỉnh kết quả theo ngữ cảnh trong hộp thoại trò chuyện.
* Thêm lệnh dịch từ Clipboard (NVDA+Control+Shift+Y).
* Lời nhắc AI được tối ưu hóa để thực thi nghiêm ngặt đầu ra ngôn ngữ đích.
* Đã sửa lỗi sự cố do các ký tự đặc biệt trong văn bản đầu vào.

## Thay đổi cho 1.5

* Đã thêm hỗ trợ cho hơn 20 ngôn ngữ mới.
* Đã triển khai Hộp thoại Tinh chỉnh Tương tác cho các câu hỏi tiếp theo.
* Đã thêm tính năng Đọc chính tả thông minh gốc.
* Đã thêm danh mục "Trợ lý thị giác" vào hộp thoại Cử chỉ nhập liệu của NVDA.
* Đã sửa lỗi COMError gặp sự cố trong các ứng dụng cụ thể như Firefox và Word.
* Đã thêm cơ chế thử lại tự động cho các lỗi máy chủ.

## Thay đổi cho 1.0

* Phát hành lần đầu.
