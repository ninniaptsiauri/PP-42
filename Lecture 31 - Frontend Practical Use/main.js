const API_URL = "https://rickandmortyapi.com/api/character";
let characterContainer = document.getElementById('characters')
characterContainer.innerHTML = ''

async function fetchCharacters() {
    let response = await fetch(API_URL);
    let data = await response.json()

    console.log(data.results);
    displayCharacters(data.results)
}

function displayCharacters(characters) {
    characters.forEach(character => {
        let cardHTML = `
            <div class="card" style="width: 16rem;">
                <img src="${character.image}" class="card-img-top" alt="..." id="card-img">
                <div class="card-body">
                    <h5 class="card-title">${character.name}</h5>
                    <p class="card-text">Species: ${character.species}</p>
                    <p class="card-text">Status: ${character.status}</p>
                    <a href="#" class="btn btn-primary">See Details</a>
                </div>
            </div>
        `;
        characterContainer.innerHTML += cardHTML
    });
}

fetchCharacters()

// for (let i = 0; i <= 10; i++) {
//     console.log(i);
// } 