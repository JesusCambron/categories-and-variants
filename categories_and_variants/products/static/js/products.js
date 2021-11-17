function addVariant(e, prefix, formClass){
    e.preventDefault()
    let variantsForm = document.querySelectorAll(formClass)
    let formNum = variantsForm.length-1
    let totalForms = document.querySelector("#id_variants-product-1-variant_category-TOTAL_FORMS")
    let container = document.querySelector("#form-container")

    let newForm = variantsForm[0].cloneNode(true)
    let formRegex = RegExp(`form-(\\d){1}-`,'g')
    formNum++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`)
    container.insertBefore(newForm, null)
    
    totalForms.setAttribute('value', `${formNum+1}`)
}