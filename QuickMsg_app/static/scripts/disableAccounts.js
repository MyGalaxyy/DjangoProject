function deleteProfile(event,userId) {
    event.preventDefault()
    const confirm = window.confirm("Hesabinizi silmek istediginize emin misiniz?, Bu islem geri alinimaz!")
    if (confirm) {
      window.location = `/profile/${userId}/remove`
    }
  }