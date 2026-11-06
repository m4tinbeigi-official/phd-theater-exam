import json
import os

repo_dir = "/Users/ricksabchez/workspace/projects/phd-theater-exam"

with open(os.path.join(repo_dir, "questions_data.json"), "r", encoding="utf-8") as f:
    questions = json.load(f)

# Read chapters
ch1_path = "/Users/ricksabchez/workspace/clients-and-collaborations/parsa-kamali/phd-theater-handbook/CH1_WORLD_THEATER_HISTORY.md"
ch2_path = os.path.join(repo_dir, "CH2_IRAN_THEATER_HISTORY.md")
ch3_path = os.path.join(repo_dir, "CH3_CONTEMPORARY_THEORIES.md")

with open(ch1_path, "r", encoding="utf-8") as f:
    ch1_content = f.read()

with open(ch2_path, "r", encoding="utf-8") as f:
    ch2_content = f.read()

with open(ch3_path, "r", encoding="utf-8") as f:
    ch3_content = f.read()

# Build index.html
html_template = """<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>سامانه جامع درسنامه و شبیه‌ساز آزمون دکتری تئاتر (کد ۲۵۰۷)</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Vazirmatn Font -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        * {
            font-family: 'Vazirmatn', sans-serif !important;
            letter-spacing: 0 !important;
        }
        body {
            background-color: #0b0f19;
            color: #f1f5f9;
        }
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #0f172a;
        }
        ::-webkit-scrollbar-thumb {
            background: #334155;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #475569;
        }
        /* Markdown prose styling */
        .prose h1 { font-size: 1.875rem; font-weight: 800; color: #38bdf8; margin-top: 1.5rem; margin-bottom: 1rem; border-bottom: 1px solid #1e293b; padding-bottom: 0.5rem; }
        .prose h2 { font-size: 1.5rem; font-weight: 700; color: #818cf8; margin-top: 1.5rem; margin-bottom: 0.75rem; }
        .prose h3 { font-size: 1.25rem; font-weight: 600; color: #c084fc; margin-top: 1.25rem; margin-bottom: 0.5rem; }
        .prose p { margin-bottom: 0.75rem; line-height: 1.8; color: #cbd5e1; }
        .prose ul, .prose ol { margin-right: 1.5rem; margin-bottom: 1rem; }
        .prose li { list-style-type: disc; margin-bottom: 0.25rem; line-height: 1.7; color: #94a3b8; }
        .prose strong { color: #f8fafc; font-weight: 700; }
        .prose table { width: 100%; border-collapse: collapse; margin-top: 1rem; margin-bottom: 1.5rem; font-size: 0.95rem; }
        .prose th, .prose td { border: 1px solid #334155; padding: 0.75rem 1rem; text-align: start; }
        .prose th { background-color: #1e293b; color: #38bdf8; font-weight: 700; }
        .prose tr:nth-child(even) { background-color: #0f172a; }
        .prose hr { border-color: #1e293b; margin: 2rem 0; }
        .tab-btn.active {
            border-bottom: 3px solid #38bdf8;
            color: #38bdf8;
            font-weight: 700;
        }
    </style>
</head>
<body class="min-h-screen flex flex-col">

    <!-- Top Navigation Bar -->
    <header class="border-b border-slate-800 bg-slate-900/80 backdrop-blur sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <span class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500 to-blue-600 flex items-center justify-center text-white font-black text-xl shadow-lg shadow-cyan-500/20">
                    ۲۵۰۷
                </span>
                <div>
                    <h1 class="text-base sm:text-lg font-bold text-white leading-tight">پایگاه جامع کنکور دکتری تئاتر</h1>
                    <p class="text-xs text-slate-400">درسنامه تخصصی، شبیه‌ساز آزمون و تحلیل پاسخنامه‌های رسمی</p>
                </div>
            </div>

            <!-- Mode Switcher -->
            <nav class="flex items-center gap-2">
                <button onclick="switchMode('handbook')" id="btn-handbook" class="px-4 py-2 rounded-lg text-sm font-semibold transition-all bg-cyan-500/10 text-cyan-400 border border-cyan-500/30">
                    📖 مطالعه درسنامه
                </button>
                <button onclick="switchMode('exam')" id="btn-exam" class="px-4 py-2 rounded-lg text-sm font-semibold transition-all text-slate-400 hover:text-white hover:bg-slate-800">
                    ✍️ شبیه‌ساز آزمون (تستی)
                </button>
            </nav>
        </div>
    </header>

    <!-- Main Container -->
    <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">

        <!-- SECTION 1: HANDBOOK (STUDY MODE) -->
        <div id="section-handbook" class="grid grid-cols-1 lg:grid-cols-4 gap-6">
            <!-- Sidebar Navigation for Chapters -->
            <aside class="lg:col-span-1 space-y-4">
                <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sticky top-24">
                    <h2 class="text-sm font-bold text-slate-300 mb-3 px-2 flex items-center gap-2">
                        <span>📚</span> فهرست سرفصل‌های تخصصی
                    </h2>
                    <div class="space-y-1">
                        <button onclick="loadChapter(1)" id="ch-btn-1" class="w-full text-start px-3 py-2.5 rounded-xl text-sm transition-all bg-cyan-500/10 text-cyan-400 font-semibold border-r-4 border-cyan-400">
                            فصل ۱: تاریخ تحلیلی تئاتر جهان
                        </button>
                        <button onclick="loadChapter(2)" id="ch-btn-2" class="w-full text-start px-3 py-2.5 rounded-xl text-sm transition-all text-slate-400 hover:bg-slate-800 hover:text-slate-200">
                            فصل ۲: ادبیات نمایشی و تئاتر در ایران
                        </button>
                        <button onclick="loadChapter(3)" id="ch-btn-3" class="w-full text-start px-3 py-2.5 rounded-xl text-sm transition-all text-slate-400 hover:bg-slate-800 hover:text-slate-200">
                            فصل ۳: نظریات معاصر و مطالعات اجرا
                        </button>
                    </div>

                    <div class="mt-6 pt-4 border-t border-slate-800">
                        <div class="p-3 bg-slate-950/60 rounded-xl border border-slate-800/80 text-xs text-slate-400 leading-relaxed">
                            💡 <strong class="text-slate-200">نکته مطالعاتی:</strong> مباحث این درسنامه منطبق بر بودجه‌بندی دفترچه‌های آزمون ۱۴۰۱ الی ۱۴۰۴ تدوین گردیده و حاوی الگوهای پرتکرار سوالات سازمان سنجش است.
                        </div>
                    </div>
                </div>
            </aside>

            <!-- Chapter Content View -->
            <div class="lg:col-span-3">
                <article class="bg-slate-900 border border-slate-800 rounded-2xl p-6 sm:p-10 shadow-xl">
                    <div id="chapter-content" class="prose max-w-none text-slate-300">
                        <!-- Markdown injected here -->
                    </div>
                </article>
            </div>
        </div>

        <!-- SECTION 2: EXAM SIMULATOR (TEST MODE) -->
        <div id="section-exam" class="hidden space-y-6">
            
            <!-- Exam Status Bar -->
            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-6 flex flex-wrap items-center justify-between gap-4 sticky top-20 z-40 shadow-xl backdrop-blur">
                <div class="flex items-center gap-4">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400 text-sm">مدت زمان:</span>
                        <span id="timer" class="font-mono text-xl font-black text-cyan-400 bg-slate-950 px-3 py-1 rounded-lg border border-slate-800">۴۵:۰۰</span>
                    </div>
                    <div class="h-6 w-px bg-slate-800"></div>
                    <div class="text-sm text-slate-400">
                        وضعیت پاسخ‌گویی: <span id="answered-count" class="font-bold text-white">۰</span> از <span id="total-count" class="font-bold text-white">۳۰</span>
                    </div>
                </div>

                <div class="flex items-center gap-3">
                    <button onclick="resetExam()" class="px-4 py-2 rounded-xl text-sm font-semibold bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors">
                        🔄 شروع مجدد
                    </button>
                    <button onclick="finishExam()" id="btn-finish" class="px-5 py-2 rounded-xl text-sm font-bold bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-white shadow-lg shadow-cyan-500/20 transition-all">
                        🏁 ثبت و دریافت کارنامه
                    </button>
                </div>
            </div>

            <!-- Score / Report Card Modal / Banner (Hidden by default) -->
            <div id="report-card" class="hidden bg-gradient-to-br from-slate-900 to-slate-950 border-2 border-cyan-500/40 rounded-2xl p-6 sm:p-8 shadow-2xl space-y-6">
                <div class="flex flex-wrap items-center justify-between gap-4 border-b border-slate-800 pb-4">
                    <div>
                        <h2 class="text-xl sm:text-2xl font-black text-white flex items-center gap-2">
                            <span>📊</span> کارنامه تحلیلی شبیه‌ساز کنکور دکتری تئاتر
                        </h2>
                        <p class="text-xs text-slate-400 mt-1">با اعمال استاندارد سازمان سنجش (نمره منفی: یک‌سوم)</p>
                    </div>
                    <span id="score-badge" class="text-2xl sm:text-3xl font-black text-cyan-400 px-4 py-2 rounded-xl bg-cyan-950/40 border border-cyan-500/30">
                        درصد کل: ۰٪
                    </span>
                </div>

                <!-- Stats Grid -->
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-4">
                    <div class="bg-slate-800/40 border border-slate-800 p-4 rounded-xl text-center">
                        <span class="text-xs text-slate-400 block mb-1">تعداد کل سوالات</span>
                        <span id="stat-total" class="text-2xl font-black text-white">۳۰</span>
                    </div>
                    <div class="bg-emerald-950/30 border border-emerald-800/40 p-4 rounded-xl text-center">
                        <span class="text-xs text-emerald-400 block mb-1">پاسخ‌های صحیح</span>
                        <span id="stat-correct" class="text-2xl font-black text-emerald-400">۰</span>
                    </div>
                    <div class="bg-rose-950/30 border border-rose-800/40 p-4 rounded-xl text-center">
                        <span class="text-xs text-rose-400 block mb-1">پاسخ‌های غلط</span>
                        <span id="stat-wrong" class="text-2xl font-black text-rose-400">۰</span>
                    </div>
                    <div class="bg-amber-950/30 border border-amber-800/40 p-4 rounded-xl text-center">
                        <span class="text-xs text-amber-400 block mb-1">بدون پاسخ</span>
                        <span id="stat-empty" class="text-2xl font-black text-amber-400">۳۰</span>
                    </div>
                </div>

                <div id="stat-feedback" class="p-4 rounded-xl bg-slate-800/30 border border-slate-700/50 text-sm text-slate-300 leading-relaxed">
                    <!-- Dynamic feedback based on score -->
                </div>
            </div>

            <!-- Questions List -->
            <div id="questions-container" class="space-y-6">
                <!-- Dynamically rendered questions -->
            </div>
        </div>

    </main>

    <!-- Footer -->
    <footer class="border-t border-slate-800 bg-slate-950 py-6 text-center text-xs text-slate-500">
        <div class="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-4">
            <p>پلتفرم مطالعاتی تخصصی کنکور دکتری تئاتر و هنرهای نمایشی (کد ۲۵۰۷) | سال‌های ۱۴۰۱ تا ۱۴۰۴</p>
            <p class="font-mono text-slate-600">Generated with PhD Theater Handbook Engine</p>
        </div>
    </footer>

    <!-- Application Script -->
    <script>
        // Questions Database
        const questions = """ + json.dumps(questions, ensure_ascii=False) + """;

        // Chapters Markdown
        const chapters = {
            1: """ + json.dumps(ch1_content, ensure_ascii=False) + """,
            2: """ + json.dumps(ch2_content, ensure_ascii=False) + """,
            3: """ + json.dumps(ch3_content, ensure_ascii=False) + """
        };

        let userAnswers = {};
        let examSubmitted = false;
        let timerInterval = null;
        let timeLeft = 45 * 60; // 45 minutes in seconds

        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            loadChapter(1);
            renderQuestions();
            updateAnsweredCount();
            startTimer();
        });

        // Mode Switcher
        function switchMode(mode) {
            const secHandbook = document.getElementById('section-handbook');
            const secExam = document.getElementById('section-exam');
            const btnHandbook = document.getElementById('btn-handbook');
            const btnExam = document.getElementById('btn-exam');

            if (mode === 'handbook') {
                secHandbook.classList.remove('hidden');
                secExam.classList.add('hidden');
                btnHandbook.className = "px-4 py-2 rounded-lg text-sm font-semibold transition-all bg-cyan-500/10 text-cyan-400 border border-cyan-500/30";
                btnExam.className = "px-4 py-2 rounded-lg text-sm font-semibold transition-all text-slate-400 hover:text-white hover:bg-slate-800";
            } else {
                secHandbook.classList.add('hidden');
                secExam.classList.remove('hidden');
                btnExam.className = "px-4 py-2 rounded-lg text-sm font-semibold transition-all bg-cyan-500/10 text-cyan-400 border border-cyan-500/30";
                btnHandbook.className = "px-4 py-2 rounded-lg text-sm font-semibold transition-all text-slate-400 hover:text-white hover:bg-slate-800";
            }
        }

        // Load Chapter Markdown
        function loadChapter(chNum) {
            for (let i = 1; i <= 3; i++) {
                const btn = document.getElementById(`ch-btn-${i}`);
                if (btn) {
                    if (i === chNum) {
                        btn.className = "w-full text-start px-3 py-2.5 rounded-xl text-sm transition-all bg-cyan-500/10 text-cyan-400 font-semibold border-r-4 border-cyan-400";
                    } else {
                        btn.className = "w-full text-start px-3 py-2.5 rounded-xl text-sm transition-all text-slate-400 hover:bg-slate-800 hover:text-slate-200";
                    }
                }
            }
            const contentDiv = document.getElementById('chapter-content');
            contentDiv.innerHTML = marked.parse(chapters[chNum]);
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        // Render Questions
        function renderQuestions() {
            const container = document.getElementById('questions-container');
            container.innerHTML = '';

            questions.forEach((q, idx) => {
                const qCard = document.createElement('div');
                qCard.id = `q-card-${q.id}`;
                qCard.className = "bg-slate-900 border border-slate-800 rounded-2xl p-6 transition-all shadow-md";

                let optionsHtml = '';
                q.options.forEach((opt, optIdx) => {
                    optionsHtml += `
                        <label class="option-label flex items-start gap-3 p-3.5 rounded-xl border border-slate-800 bg-slate-950/60 hover:bg-slate-800/50 cursor-pointer transition-all" id="opt-label-${q.id}-${optIdx}">
                            <input type="radio" name="question-${q.id}" value="${optIdx}" onchange="selectAnswer(${q.id}, ${optIdx})" class="mt-1 w-4 h-4 text-cyan-500 focus:ring-cyan-400 bg-slate-900 border-slate-700">
                            <span class="text-sm text-slate-300 leading-relaxed font-normal">${opt}</span>
                        </label>
                    `;
                });

                qCard.innerHTML = `
                    <div class="flex items-center justify-between gap-4 mb-4">
                        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-slate-800 text-cyan-400 border border-slate-700">
                            سوال ${idx + 1} | ${q.category}
                        </span>
                        <span id="q-status-${q.id}" class="text-xs text-slate-500">پاسخ داده نشده</span>
                    </div>
                    <h3 class="text-base font-bold text-slate-100 leading-relaxed mb-4">
                        ${q.question}
                    </h3>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-4">
                        ${optionsHtml}
                    </div>
                    <!-- Detailed Explanation & Trap Box (Visible after submission) -->
                    <div id="explanation-${q.id}" class="hidden mt-4 pt-4 border-t border-slate-800/80 space-y-2">
                        <div class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs sm:text-sm text-slate-300 leading-relaxed">
                            <strong class="text-emerald-400 block mb-1">✅ تحلیل تشریحی پاسخ:</strong>
                            ${q.explanation}
                        </div>
                        <div class="p-3.5 rounded-xl bg-amber-950/20 border border-amber-900/30 text-xs sm:text-sm text-amber-300/90 leading-relaxed">
                            <strong class="text-amber-400 block mb-1">⚠️ تحلیل دام تستی طراح:</strong>
                            ${q.trap}
                        </div>
                    </div>
                `;
                container.appendChild(qCard);
            });
            document.getElementById('total-count').innerText = questions.length;
        }

        // Handle Answer Selection
        function selectAnswer(qId, optIdx) {
            if (examSubmitted) return;
            userAnswers[qId] = optIdx;
            const statusEl = document.getElementById(`q-status-${qId}`);
            if (statusEl) {
                statusEl.innerText = "ثبت شد";
                statusEl.className = "text-xs text-cyan-400 font-semibold";
            }
            updateAnsweredCount();
        }

        function updateAnsweredCount() {
            const count = Object.keys(userAnswers).length;
            document.getElementById('answered-count').innerText = count;
        }

        // Timer
        function startTimer() {
            if (timerInterval) clearInterval(timerInterval);
            timerInterval = setInterval(() => {
                if (timeLeft <= 0) {
                    clearInterval(timerInterval);
                    finishExam();
                    return;
                }
                timeLeft--;
                const minutes = Math.floor(timeLeft / 60);
                const seconds = timeLeft % 60;
                document.getElementById('timer').innerText = 
                    `${String(minutes).padStart(2, '۰')}:${String(seconds).padStart(2, '۰')}`;
            }, 1000);
        }

        // Finish Exam & Calculate Score
        function finishExam() {
            if (examSubmitted) return;
            examSubmitted = true;
            clearInterval(timerInterval);

            let correct = 0;
            let wrong = 0;
            let empty = 0;

            questions.forEach(q => {
                const userAns = userAnswers[q.id];
                const card = document.getElementById(`q-card-${q.id}`);
                const expBox = document.getElementById(`explanation-${q.id}`);
                expBox.classList.remove('hidden');

                if (userAns === undefined) {
                    empty++;
                } else if (userAns === q.answer) {
                    correct++;
                    card.classList.add('border-emerald-500/50', 'bg-emerald-950/10');
                    document.getElementById(`opt-label-${q.id}-${userAns}`).classList.add('border-emerald-500', 'bg-emerald-900/20');
                } else {
                    wrong++;
                    card.classList.add('border-rose-500/50', 'bg-rose-950/10');
                    document.getElementById(`opt-label-${q.id}-${userAns}`).classList.add('border-rose-500', 'bg-rose-900/20');
                    // Highlight the correct option
                    document.getElementById(`opt-label-${q.id}-${q.answer}`).classList.add('border-emerald-500', 'bg-emerald-900/20');
                }
            });

            // Calculate percentage with 1/3 negative marking
            const totalQ = questions.length;
            const rawScore = (correct * 3 - wrong) / (totalQ * 3);
            const scorePercent = Math.max(0, Math.round(rawScore * 100));

            // Show report card
            const reportEl = document.getElementById('report-card');
            reportEl.classList.remove('hidden');
            document.getElementById('score-badge').innerText = `درصد تراز نهایی: ${scorePercent}٪`;
            document.getElementById('stat-total').innerText = totalQ;
            document.getElementById('stat-correct').innerText = correct;
            document.getElementById('stat-wrong').innerText = wrong;
            document.getElementById('stat-empty').innerText = empty;

            let feedbackText = "";
            if (scorePercent >= 70) {
                feedbackText = "🔥 **عالی! رتبه تک‌رقمی تضمینی:** تسلط شما بر تاریخ تئاتر جهان، نظریات پست‌دراماتیک و مباحث مطالعات اجرا فوق‌العاده است. با این تراز در بهترین دانشگاه‌های دولتی تهران پذیرفته خواهید شد.";
            } else if (scorePercent >= 45) {
                feedbackText = "✨ **بسیار خوب و در محدوده قبولی نهایی:** عملکرد مناسبی داشته‌اید. با مرور فصل‌های دوم و سوم (تئاتر در ایران و نظریات معاصر اجرا) و کنترل نمره منفی می‌توانید رتبه خود را به زیر ۲۰ ارتقا دهید.";
            } else {
                feedbackText = "📌 **نیاز به مرور دقیق‌تر درسنامه:** دام‌های تستی طراحان کنکور دکتری به ویژه در حوزه کمدیا دلارته، مکاتب نقد و تئاتر شرق چالش‌برانگیز بوده‌اند. توصیه می‌شود یک دور کامل سرفصل‌های ۳ گانه درسنامه را با دقت مرور کنید.";
            }
            document.getElementById('stat-feedback').innerHTML = marked.parse(feedbackText);

            reportEl.scrollIntoView({ behavior: 'smooth' });
            document.getElementById('btn-finish').innerText = "آزمون به پایان رسید";
            document.getElementById('btn-finish').disabled = true;
            document.getElementById('btn-finish').classList.add('opacity-50', 'cursor-not-allowed');
        }

        // Reset Exam
        function resetExam() {
            if (confirm("آیا تمایل دارید آزمون را از ابتدا مجدداً آغاز کنید؟")) {
                userAnswers = {};
                examSubmitted = false;
                timeLeft = 45 * 60;
                document.getElementById('report-card').classList.add('hidden');
                document.getElementById('btn-finish').innerText = "🏁 ثبت و دریافت کارنامه";
                document.getElementById('btn-finish').disabled = false;
                document.getElementById('btn-finish').classList.remove('opacity-50', 'cursor-not-allowed');
                renderQuestions();
                updateAnsweredCount();
                startTimer();
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        }
    </script>
</body>
</html>
"""

with open(os.path.join(repo_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_template)

print("Generated index.html successfully with total bytes:", len(html_template))
