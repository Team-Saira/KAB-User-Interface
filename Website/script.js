function handleFormSubmit(event) {
  event.preventDefault();

  const data = new FormData(event.target);

  const formJSON = Object.fromEntries(data.entries());

  // for multi-selects, we need special handling
  //formJSON.multi = data.getAll('multi');

  const results = document.querySelector('.results pre');
  results.innerText = JSON.stringify(formJSON, null, 2);
  FileSystem.writeFile('results.json', results, 'utf8', callback);
}

const form = document.querySelector('.entry-form');
form.addEventListener('submit', handleFormSubmit);