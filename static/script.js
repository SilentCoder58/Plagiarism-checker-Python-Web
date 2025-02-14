document.getElementById("plagiarismForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const sample1Text = document.getElementById("sample1").value;
    const sample2Text = document.getElementById("sample2").value;

    if (!sample1Text || !sample2Text) {
        alert("Please enter text in both samples.");
        return;
    }

    const formData = new FormData();
    formData.append('sample1', sample1Text);
    formData.append('sample2', sample2Text);

    fetch('/check_plagiarism', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerText = data.error;
        } else {
            document.getElementById("result").innerText = `Plagiarism Similarity: ${data.similarity_percentage}`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    });
});
