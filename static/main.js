// Show loading spinner on form submit
const form = document.querySelector('form');
const spinner = document.createElement('div');
spinner.className = 'spinner';
spinner.innerHTML = '<div></div><div></div><div></div><div></div>';

if (form) {
    form.addEventListener('submit', function(e) {
        const textarea = form.querySelector('textarea');
        if (!textarea.value.trim()) {
            e.preventDefault();
            textarea.focus();
            alert('Please paste your buggy code before submitting!');
            return;
        }
        document.body.appendChild(spinner);
    });
}

// Copy to clipboard functionality
const copyBtn = document.getElementById('copy-btn');
if (copyBtn) {
    copyBtn.addEventListener('click', function() {
        const codeBlock = document.getElementById('fixed-code-block');
        if (codeBlock) {
            navigator.clipboard.writeText(codeBlock.innerText);
            copyBtn.innerText = 'Copied!';
            setTimeout(() => copyBtn.innerText = 'Copy', 1200);
        }
    });
}
