document.addEventListener('DOMContentLoaded', function () {
    const fullscreenVideo = document.querySelector('.fullscreen-video');
    const videoIframe = fullscreenVideo.querySelector('iframe');
    const videoTitle = fullscreenVideo.querySelector('.video-title');
    const videoMeta = fullscreenVideo.querySelector('.video-meta');
    const closeVideo = fullscreenVideo.querySelector('.close-video');

    // Function to open fullscreen video
    function openFullscreenVideo(videoUrl, title, meta) {
        videoIframe.src = videoUrl;
        console.log(">>>>>>>>", videoUrl)
        videoTitle.textContent = title;
        videoMeta.textContent = meta;
        fullscreenVideo.classList.add('active');
        document.body.style.overflow = 'hidden'; // Prevent scrolling when video is open
    }

    // Function to close fullscreen video
    function closeFullscreenVideo() {
        videoIframe.src = '';
        fullscreenVideo.classList.remove('active');
        document.body.style.overflow = ''; // Re-enable scrolling
    }

    // Handle click on play overlay buttons
    const playButtons = document.querySelectorAll('.play-button');
    playButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            e.stopPropagation();
            const videoUrl = this.getAttribute('data-video');
            const title = this.getAttribute('data-title');
            const meta = this.getAttribute('data-meta');
            openFullscreenVideo(videoUrl, title, meta);
        });
    });

    // Handle click on listen buttons
    const listenButtons = document.querySelectorAll('.podcast-button');
    listenButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            e.stopPropagation();
            const videoUrl = this.getAttribute('data-video');
            const title = this.getAttribute('data-title');
            const meta = this.getAttribute('data-meta');
            openFullscreenVideo(videoUrl, title, meta);
        });
    });
    // console.log(meta)
    // Close video when clicking the close button
    closeVideo.addEventListener('click', function () {
        closeFullscreenVideo();
    });

    // Close video when pressing ESC key
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && fullscreenVideo.classList.contains('active')) {
            closeFullscreenVideo();
        }
    });

    // Close video when clicking outside the video container
    fullscreenVideo.addEventListener('click', function (e) {
        if (e.target === fullscreenVideo) {
            closeFullscreenVideo();
        }
    });
});
