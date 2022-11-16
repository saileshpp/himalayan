// let script = document.createElement('script')
// script.type = 'text/javascript'
// script.scr = 'https://cdnjs.cloudflare.com/ajax/libs/tinymce/5.0.0/tinymce.min.js'
// document.head.appendChild(script)

// script.onload = function () {
//     tinymce.init({
//         selector: '#id_day_1',
//         plugins: 'anchor autolink charmap codesample emoticons image link lists media searchreplace table visualblocks wordcount',
//         toolbar: 'undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | link image media table | align lineheight | numlist bullist indent outdent | emoticons charmap | removeformat',
//     });
// }

window.addEventListener('load', (event) => {
    tinymce.init({
        selector: '#id_day_1',
        // inline: true,
        plugins: 'anchor autolink charmap codesample emoticons image link lists media searchreplace table visualblocks wordcount',
        toolbar: 'undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | align lineheight | table | removeformat', 
        table_border_widths: [
            { title: 'small', value: '1px' },
            { title: 'medium', value: '3px' },
            { title: 'large', value: '5px' },
        ]
    });
});