const form = document.querySelector('.entry-form');
form.addEventListener('submit', handleFormSubmit);

function handleFormSubmit(event) {

$.ajax({
type:"POST",
url:"/input",
data:{'addresses':$('#addr').val(), 'cites':$('#city').val(), 'zips':$('#zip').val(), 'latitudes':$('#lat').val(), 'longitudes':$('#long').val(), 'states':$('#state').val()},
contentType: "application/json",
dataType: 'json',
success:function(data){

    event.preventDefault();
    alert("went through ajax")



    const entry = new FormData(event.target);

    const formJSON = Object.fromEntries(entry.entries());

// for multi-selects, we need special handling
//formJSON.multi = entry.getAll('multi');

const results = document.querySelector('.results pre');
results.innerText = JSON.stringify(formJSON, null, 2);
//FileSystem.writeFile('results.json', results, 'utf8', callback);

}});
}

/*
function handleFormSubmit(event) {

event.preventDefault();

const data = new FormData(event.target);

const formJSON = Object.fromEntries(data.entries());

// for multi-selects, we need special handling
//formJSON.multi = data.getAll('multi');

const results = document.querySelector('.results pre');
results.innerText = JSON.stringify(formJSON, null, 2);
//FileSystem.writeFile('results.json', results, 'utf8', callback);

}));
}

const form = document.querySelector('.entry-form');
form.addEventListener('submit', handleFormSubmit);
*/