    // Function to handle the search and display quotes
    function searchQuotes() {
        const searchInput = document.getElementById('searchInput').value.toLowerCase();
        console.log('This is the input you typed:', searchInput);

        fetch(`/data?query_html=${encodeURIComponent(searchInput)}`)
            .then(response => response.json())
            .then(data => {
                console.log(data);

                // Check if data has a key and element exists
                const key = Object.keys(data)[0]?.toLowerCase();
                if (!key) {
                    console.error('No valid data received');
                    return;
                }

                const element = document.getElementById(key);
                if (element) {
                    console.log('This is the element:', element);
                    element.scrollIntoView({ behavior: 'smooth' });
                } else {
                    console.error('Element not found for:', key);
                }

                const resultDiv = document.getElementById('result');
                resultDiv.innerHTML = ''; // Clear any previous results

                if (data.error) {
                    resultDiv.innerText = data.error;
                } else {
                    // Display the search results
                    for (const [author, quotes] of Object.entries(data)) {
                        const authorDiv = document.createElement('div');
                        authorDiv.innerHTML = `<h3>${author}</h3><p>${quotes.join('<br>')}</p>`;
                        resultDiv.appendChild(authorDiv);
                    }
                }
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }

    // Ensure the DOM is fully loaded before running scripts
    document.addEventListener('DOMContentLoaded', function () {
        // Adding event listener for clicks on dynamically loaded cards
        const container = document.getElementById('container');

        if (container) {
            const allItems = container.querySelectorAll('.card');
            allItems.forEach(function (item) {
                item.addEventListener('click', function () {
                    console.log("Card clicked:", item.id);
                    window.location.href = `/author/${item.id.toLowerCase()}`;
                });
            });

            // Event delegation for buttons inside the container
            container.addEventListener('click', function (event) {
                if (event.target && event.target.matches('.download-image')) {
                    const imageId = event.target.getAttribute('data-image-id');
                    const imageUrl = document.getElementById(`image-${imageId}`).src;
                    const a = document.createElement("a");
                    a.href = imageUrl;
                    a.download = "quote-image";
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                }

                if (event.target && event.target.matches('.whatsapp-share')) {
                    const imageId = event.target.getAttribute('data-image-id');
                    const imageUrl = document.getElementById(`image-${imageId}`).src;
                    const whatsappUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent("Check this image: " + imageUrl)}`;
                    window.open(whatsappUrl, '_blank');
                }
            });
        } else {
            console.error('Container element not found.');
        }
    });
