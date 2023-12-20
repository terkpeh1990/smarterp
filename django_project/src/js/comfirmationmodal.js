document.addEventListener('DOMContentLoaded', function () {
  var deleteAnchors = document.getElementsByClassName('delete-record')
  var deleteModalAnchor = document.getElementById('deleteModalAnchor')
  Array.from(deleteAnchors).forEach(function (anchor) {
    anchor.addEventListener('click', function (event) {
      event.preventDefault()
      var recordId = this.getAttribute('data-record-id')
      deleteModalAnchor.setAttribute('data-record-id', recordId)
      deleteModalAnchor.setAttribute(
        'href',
        '/authentication/group/' + recordId + '/delete/',
      )
      deleteModalAnchor.style.display = 'block'
    })
  })
})


