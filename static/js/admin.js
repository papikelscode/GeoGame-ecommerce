const productInfo = async () =>{
    
    try { 
        const Details = {}
        Details.productname = document.getElementById("productname").value
        Details.productprice = document.getElementById("productprice").value
        Details.productimage = document.getElementById("productimage").value
     
      
        console.log("details",Details);
        


        const resp = await  axios.post('/dashboard', Details,{
            headers:{
                'Content-Type': 'application/json'
            }
            
        });
        
      
    } catch (error) {
      console.log(error.response.data);
    }


  }
