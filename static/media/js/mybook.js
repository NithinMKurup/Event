function showAlert(message) {
    alert(message);
}

window.onload = function() {
    var messages = JSON.parse('{{ messages_json|escapejs }}');
    messages.forEach(function(message) {
        showAlert(message);
    });
}
