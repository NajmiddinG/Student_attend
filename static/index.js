const loader = document.querySelector('.loader');

const loading = () => {
    setTimeout(() => {
        loader.style.display = 'none';
        document.getElementById('page').style.display = 'block';
    }, 1000);
};