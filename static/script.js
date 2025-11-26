document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const eventCards = document.querySelectorAll('.event-card');
    const noResultsMsg = document.getElementById('noResults');

    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();
        let visibleCount = 0;

        eventCards.forEach(card => {
            const title = card.dataset.title.toLowerCase();
            const speakers = card.dataset.speakers.toLowerCase();
            const category = card.dataset.category.toLowerCase();

            if (title.includes(query) || speakers.includes(query) || category.includes(query)) {
                card.classList.remove('hidden');
                visibleCount++;
            } else {
                card.classList.add('hidden');
            }
        });

        if (visibleCount === 0) {
            noResultsMsg.classList.remove('hidden');
        } else {
            noResultsMsg.classList.add('hidden');
        }
    });
});
