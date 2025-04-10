// Mobile navigation functionality
const burger = document.querySelector('.burger');
const nav = document.querySelector('.nav-links');
const navLinks = document.querySelectorAll('.nav-links li');
const overlay = document.querySelector('.nav-overlay');

burger.addEventListener('click', () => {
    // Toggle Nav
    nav.classList.toggle('nav-active');

    // Toggle Overlay
    overlay.classList.toggle('active');

    // Toggle Burger Animation
    burger.classList.toggle('toggle');

    // Animate Links
    navLinks.forEach((link, index) => {
        if (nav.classList.contains('nav-active')) {
            link.style.animation = `slideDown 0.4s ease forwards ${index / 7}s`;
        } else {
            link.style.animation = '';
        }
    });
});

// Close mobile menu when clicking overlay
overlay.addEventListener('click', () => {
    nav.classList.remove('nav-active');
    overlay.classList.remove('active');
    burger.classList.remove('toggle');

    navLinks.forEach(link => {
        link.style.animation = '';
    });
});
// Mobile: toggle dropdown for "Blog"
const dropdown = document.querySelector('.dropdown');
const dropTrigger = document.querySelector('.drop-trigger');

dropTrigger.addEventListener('click', (e) => {
    // Only on mobile
    if (window.innerWidth <= 768) {
        e.preventDefault();
        dropdown.classList.toggle('active');
    }
});

document.querySelector('.back-button').addEventListener('click', function (e) {
    e.preventDefault();
    window.history.back();
});

// Book data
const books = [
    {
        id: 1,
        title: "Государь",
        author: "Николо Макиавелли",
        image: "/api/placeholder/400/300",
        description: "«Государь» — политический трактат Никколо Макиавелли, написанный им в 1513 году. В этом произведении Макиавелли рассматривает различные типы государств, способы их приобретения и удержания, а также качества, необходимые правителю для успешного управления. Книга стала одним из краеугольных камней современной политической философии и породила термин «макиавеллизм».",
        quotes: [
            "Люди всегда злы, если их не принуждает к добру необходимость.",
            "Цель оправдывает средства.",
            "Лучше быть страшным, чем смешным, ибо страха боятся, а над смешным смеются."
        ],
        discussions: [
            {
                title: "Актуальность идей Макиавелли в современной политике",
                description: "Насколько применимы идеи Макиавелли к современным политическим реалиям? Изменились ли основы политического лидерства за прошедшие века?"
            },
            {
                title: "Этика и политика: конфликт или гармония?",
                description: "Обсуждение противоречий между моральными принципами и политической целесообразностью в контексте «Государя»."
            }
        ],
        comments: [
            {
                author: "Анна Соколова",
                date: "2 апреля 2025",
                text: "Поразительно, насколько современно звучат многие тезисы Макиавелли. Особенно интересны его рассуждения о природе человека и склонности людей к эгоизму."
            },
            {
                author: "Михаил Кузнецов",
                date: "28 марта 2025",
                text: "Считаю, что «Государь» — обязательное чтение для понимания политических процессов. Макиавелли был одним из первых, кто описал политику такой, какая она есть, без морализаторства."
            }
        ]
    },
    {
        id: 2,
        title: "Критика чистого разума",
        author: "Иммануил Кант",
        image: "/api/placeholder/400/300",
        description: "«Критика чистого разума» — фундаментальный труд немецкого философа Иммануила Канта, опубликованный в 1781 году. В этой работе Кант предпринял попытку определить границы и возможности человеческого познания, исследуя соотношение эмпирического опыта и априорных форм мышления. Книга стала отправной точкой для развития немецкого идеализма и оказала огромное влияние на всю последующую философию.",
        quotes: [
            "Мысли без содержания пусты, созерцания без понятий слепы.",
            "Две вещи наполняют душу всегда новым и все более сильным удивлением и благоговением, чем чаще и продолжительнее мы размышляем о них, — это звездное небо надо мной и моральный закон во мне.",
            "Разум должен подходить к природе не в качестве ученика, который слушает все, что учитель хочет сказать, а в качестве судьи, который заставляет свидетелей отвечать на вопросы, которые он сам поставил."
        ],
        discussions: [
            {
                title: "Кантианский дуализм: проблема соединения феноменального и ноуменального миров",
                description: "Обсуждение противоречий в теории познания Канта и попыток их разрешения."
            },
            {
                title: "Влияние теории познания Канта на современную науку",
                description: "Как идеи Канта о познании отражаются в современной эпистемологии и научной методологии?"
            }
        ],
        comments: [
            {
                author: "Игорь Соловьев",
                date: "1 апреля 2025",
                text: "Один из самых сложных философских текстов, с которыми мне приходилось иметь дело. Понадобилось несколько прочтений, чтобы уловить основные идеи Канта."
            },
            {
                author: "Елена Морозова",
                date: "20 марта 2025",
                text: "Переворот, совершенный Кантом в философии, действительно сравним с коперниканским переворотом в астрономии. Его идея о том, что не познание подстраивается под предметы, а предметы — под наши способы познания, радикально изменила философский ландшафт."
            }
        ]
    },
    {
        id: 3,
        title: "Так говорил Заратустра",
        author: "Фридрих Ницше",
        image: "/api/placeholder/400/300",
        description: "«Так говорил Заратустра» — философский роман Фридриха Ницше, написанный между 1883 и 1885 годами. В этом произведении Ницше излагает свои идеи о сверхчеловеке, воле к власти, вечном возвращении и преодолении христианской морали. Книга написана в форме притч и речей пророка Заратустры и стала одним из самых влиятельных философских произведений XIX века.",
        quotes: [
            "Человек есть нечто, что должно превзойти.",
            "Бог умер: теперь хотим мы, чтобы жил сверхчеловек.",
            "Кто сражается с чудовищами, тому следует остерегаться, чтобы самому при этом не стать чудовищем. И если ты долго смотришь в бездну, то бездна тоже смотрит в тебя."
        ],
        discussions: [
            {
                title: "Идея сверхчеловека: предсказание или предупреждение?",
                description: "Обсуждение различных интерпретаций концепции сверхчеловека у Ницше."
            },
            {
                title: "Ницше и нигилизм",
                description: "Был ли Ницше нигилистом или его философия представляет собой попытку преодоления нигилизма?"
            }
        ],
        comments: [
            {
                author: "Алексей Воронин",
                date: "5 апреля 2025",
                text: "Поэтический язык Ницше делает его философию особенно привлекательной. В «Заратустре» мысль и форма неразрывно связаны, что создает совершенно особое впечатление от чтения."
            },
            {
                author: "Ольга Семенова",
                date: "27 марта 2025",
                text: "Идея вечного возвращения — одна из самых сложных и противоречивых у Ницше. До сих пор не могу определиться, считать ли ее метафорой или онтологическим принципом."
            }
        ]
    },
    {
        id: 4,
        title: "Миф о Сизифе",
        author: "Альбер Камю",
        image: "/api/placeholder/400/300",
        description: "«Миф о Сизифе» — философское эссе Альбера Камю, опубликованное в 1942 году. В этой работе Камю развивает свою философию абсурда, рассматривая проблему смысла человеческого существования в мире, лишенном метафизических оснований. Центральный вопрос эссе — самоубийство и его философское обоснование. Камю приходит к выводу о необходимости бунта против абсурда и утверждения жизни вопреки ее бессмысленности.",
        quotes: [
            "Существует лишь одна по-настоящему серьезная философская проблема — проблема самоубийства.",
            "Абсурд рождается в столкновении между человеческим призывом и неразумным молчанием мира.",
            "Нужно представлять себе Сизифа счастливым."
        ],
        discussions: [
            {
                title: "Экзистенциализм и абсурд: пути преодоления",
                description: "Обсуждение различных способов противостояния абсурду в философии экзистенциализма."
            },
            {
                title: "Камю и Сартр: сравнительный анализ",
                description: "Сходства и различия в понимании свободы, ответственности и абсурда у двух великих экзистенциалистов."
            }
        ],
        comments: [
            {
                author: "Дмитрий Николаев",
                date: "3 апреля 2025",
                text: "Удивительно, как Камю удается говорить о таких мрачных вещах и при этом приходить к утверждению жизни. Его философия абсурда парадоксальным образом оптимистична."
            },
            {
                author: "Мария Белова",
                date: "25 марта 2025",
                text: "Метафора Сизифа как человека, осознающего бессмысленность своего труда, но находящего в нем свое достоинство, остается одной из самых мощных в философии XX века."
            }
        ]
    }
];

// Check if user is authenticated
const chatForm = document.querySelector('.chat-form');
if (chatForm) {
    // Handle form submission with AJAX
    chatForm.addEventListener('submit', function (e) {
        e.preventDefault();

        // Get the form data
        const formData = new FormData(chatForm);

        // Submit the form via AJAX
        fetch(window.location.href, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
            }
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Clear the textarea
                    const textarea = chatForm.querySelector('textarea');
                    if (textarea) {
                        textarea.value = '';
                    }

                    // Show success message
                    const successMessage = document.createElement('div');
                    successMessage.className = 'success-message';
                    successMessage.textContent = 'Message sent!';
                    chatForm.prepend(successMessage);

                    // Remove success message after animation
                    setTimeout(() => {
                        successMessage.remove();
                    }, 4000);

                    // Refresh chat messages
                    refreshChat();
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
} else {
    // If form doesn't exist, create login button
    createLoginButton();
}

// Function to refresh chat messages
function refreshChat() {
    fetch(window.location.href + '?format=json')
        .then(response => response.json())
        .then(data => {
            if (data.messages) {
                // Update chat messages
                const chatMessages = document.getElementById('chat-messages');
                chatMessages.innerHTML = '';

                data.messages.forEach(message => {
                    const messageElement = document.createElement('p');
                    messageElement.innerHTML = `<strong>${message.author}:</strong> ${message.content} <small>${message.created_at}</small>`;
                    chatMessages.appendChild(messageElement);
                });

                // Scroll to bottom
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }
        })
        .catch(error => {
            console.error('Error refreshing chat:', error);
        });
}

// Create login button if user is not authenticated
function createLoginButton() {
    const chatFormContainer = document.querySelector('.chat-form');
    if (!chatFormContainer) {
        const formArea = document.querySelector('#chat-messages').nextElementSibling;
        if (formArea) {
            const loginContainer = document.createElement('div');
            loginContainer.className = 'login-container';
            loginContainer.innerHTML = `
                    <p>You must be logged in to send messages</p>
                    <a href="/login/?next=${window.location.pathname}" class="login-button">Log In</a>
                `;
            formArea.parentNode.replaceChild(loginContainer, formArea);
        } else {
            const loginContainer = document.createElement('div');
            loginContainer.className = 'login-container';
            loginContainer.innerHTML = `
                    <p>You must be logged in to send messages</p>
                    <a href="/login/?next=${window.location.pathname}" class="login-button">Log In</a>
                `;
            document.querySelector('#chat-messages').insertAdjacentElement('afterend', loginContainer);
        }
    }
}

// Auto-refresh every 10 seconds
setInterval(refreshChat, 10000);
const chatMessages = document.getElementById('chat-messages');
chatMessages.scrollTop = chatMessages.scrollHeight;

// Add user-message class to current user's messages if it wasn't added by Django template
if ('{{ user.username }}') {
    const allMessages = chatMessages.querySelectorAll('p');
    allMessages.forEach(message => {
        const usernameElement = message.querySelector('strong');
        if (usernameElement && usernameElement.textContent.trim() === '{{ user.username }}') {
            message.classList.add('user-message');
        }
    });
}