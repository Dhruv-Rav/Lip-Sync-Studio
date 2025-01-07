document.addEventListener('DOMContentLoaded', function() {
    const imageUpload = document.getElementById('image-upload');
    const audioUpload = document.getElementById('audio-upload');
    const uploadButton = document.getElementById('upload-button');
    const processingFeedback = document.getElementById('processing-feedback');
    const outputSection = document.getElementById('output-section');
    const outputVideo = document.getElementById('output-video');
    const downloadButton = document.getElementById('download-button');

    imageUpload.addEventListener('click', () => imageUpload.querySelector('input').click());
    audioUpload.addEventListener('click', () => audioUpload.querySelector('input').click());

    uploadButton.addEventListener('click', async function() {
        const imageFile = imageUpload.querySelector('input').files[0];
        const audioFile = audioUpload.querySelector('input').files[0];

        if (!imageFile || !audioFile) {
            alert('Please upload both image and audio files.');
            return;
        }

        const formData = new FormData();
        formData.append('image', imageFile);
        formData.append('audio', audioFile);

        processingFeedback.classList.remove('hidden');

        const response = await fetch('/process', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        processingFeedback.classList.add('hidden');

        if (response.ok) {
            outputSection.classList.remove('hidden');
            outputVideo.src = result.video_url;
            downloadButton.href = result.video_url;
            downloadButton.download = 'lip_sync_video.mp4';
        } else {
            alert(result.error);
        }
    });
});