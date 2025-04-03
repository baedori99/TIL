# 📺 YouTube Comment Crawler

A simple yet effective crawler that extracts user comments, IDs, and like counts from a specific YouTube video using Selenium and organizes them into a structured DataFrame.

---

## 📌 Project Overview

This project was created to analyze YouTube comment sentiment for specific videos such as vlogs, sports highlights, or controversial content.  
The crawler is tailored to collect comment metadata including:

- **User ID**
- **Comment text**
- **Like count**
- **Video ID (for reference)**

> 💡 Originally developed to test the sentiment around certain videos using keyword analysis and NLP later on.

---

## 🛠️ Technologies Used

| Component   | Library / Tool |
|-------------|----------------|
| Web Scraping | Selenium       |
| Browser      | ChromeDriver   |
| Automation   | ActionChains   |
| Data Storage | pandas         |

---

## ⚙️ Features

- Auto-scrolls through YouTube comments (configurable scroll depth)
- Skips replies (top-level comments only)
- Extracts:
  - Commenter's ID
  - Comment content
  - Number of likes
  - Video ID (via URL)
- Outputs results to a clean `pandas.DataFrame`

---

## ▶️ How to Run

### 1. Install Requirements

```bash
pip install selenium pandas

2. Download ChromeDriver
Make sure it matches your Chrome version:
👉 https://sites.google.com/chromium.org/driver/

3. Run the notebook
Open youtube_crawler.ipynb in Jupyter and follow cell-by-cell execution.

🧪 Sample Output (Head)
Video ID	ID	Comment	Likes
SsJg6x-inFw	@user123	한화 너무 잘한다! 대박 경기!	237
SsJg6x-inFw	@baseballfan	작전야구를 다시 보게 되다니 ㅠㅠ 감사합니다 감독님	58

🚫 Limitations
Only works with public YouTube videos.
Does not extract nested replies.
Limited by YouTube's dynamic content loading structure (scroll cap).

📚 Future Plans
Add sentiment analysis (with Huggingface/BERT or ChatGPT)
Include reply-level comment crawling
Export to CSV or database for scalable analysis
