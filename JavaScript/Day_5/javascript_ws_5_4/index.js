const URL = "https://ws.audioscrobbler.com/2.0/"
const API_KEY = "89cd9d59c62295df71a81c67a914aa21"
const btn = document.querySelector('.search-box__button')
const inputBox = document.querySelector('.search-box__input')
const fetchAlbums = function (event) {
  axios({
    url:URL,
    params: {
      method : 'album.search',
      album: inputBox.value,
      api_key:"89cd9d59c62295df71a81c67a914aa21",
      format:'json'
    }
  })
  .then((response) => {
    
    
    return response.data.results.albummatches.album
  })
  .then((response) => {

    response.forEach((album) => {
      const searchBox = document.querySelector('.search')
      const cardImg = document.createElement('img')
      cardImg.src = album.image[1]['#text']
      
      const card = document.createElement('div')
      card.classList.add('search-result__card')

      card.append(cardImg)

      const artistName = document.createElement('h2')
      artistName.innerText = album.artist

      const albumName = document.createElement('p')
      albumName.innerText = album.name
      card.appendChild(artistName)
      card.appendChild(albumName)
      searchBox.appendChild(card)
    
    })
  })
}
btn.addEventListener('click', fetchAlbums)
