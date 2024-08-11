function updatePrice(type) {
    if (type === 'min') {
        let min_price = document.getElementById('min_price').value;
        document.getElementById('min_price_display').textContent = min_price;
    } else if (type === 'max') {
        let max_price = document.getElementById('max_price').value;
        document.getElementById('max_price_display').textContent = max_price;
    }
}

// Инициализация начальных значений при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    updatePrice('min');
    updatePrice('max');
});