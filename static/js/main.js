document.getElementById('chatbox-send-button').addEventListener('click', sendMessage);
document.getElementById('chatbox-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    const inputField = document.getElementById('chatbox-input');
    const message = inputField.value.trim();
    
    if (message) {
        const chatboxBody = document.getElementById('chatbox-body');
        const userMessage = document.createElement('div');
        userMessage.classList.add('chatbox-message', 'user');
        userMessage.innerText = message;
        chatboxBody.appendChild(userMessage);
        
        // Enviar mensagem para o backend e receber resposta
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message }),
        })
        .then(response => response.json())
        .then(data => {
            const botMessage = document.createElement('div');
            botMessage.classList.add('chatbox-message', 'bot');
            botMessage.innerText = data.response;
            chatboxBody.appendChild(botMessage);
            chatboxBody.scrollTop = chatboxBody.scrollHeight;
        });
        
        inputField.value = '';
    }
}
