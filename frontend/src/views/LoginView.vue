<template>
    <div class="login">
      <div id="login-box">
        <h1>Login</h1>
        <div class="form">
          <div class="item">
            <i class="fa fa-github-alt" style="font-size: 24px"></i>
            <input type="text" placeholder="Username" />
          </div>
          <div class="item">
            <i class="fa fa-search" style="font-size: 24px"></i>
            <input type="text" placeholder="Password" />
          </div>
        </div>
        <button>Login</button>
      </div>
    </div>
  </template>
  
  <style scoped lang="scss">
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: black;
  }
  .login {
    width: 100%;
    height: 100%;
    z-index: -1;
    position: absolute;
    background: url(../assets/images/background.png);
    background-size: 100% 100%;
  }
  #login-box {
    width: 30%;
    height: auto;
    margin: 0 auto;
    margin-top: 13%;
    text-align: center;
    background: #00000060;
    padding: 20px 50px;
  }
  #login-box h1 {
    color: #fff;
  }
  #login-box .form .item {
    margin-top: 15px;
  }
  #login-box .form .item i {
    font-size: 18px;
    color: #fff;
  }
  #login-box .form .item input {
    width: 180px;
    font-size: 18px;
    border: 0;
    border-bottom: 2px solid #fff;
    padding: 5px 10px;
    background: #ffffff00;
    color: #fff;
  }
  #login-box button {
    margin-top: 20px;
    width: 190px;
    height: 30px;
    font-size: 20px;
    font-weight: 700;
    color: #fff;
    background-image: linear-gradient(to right, #74ebd5 0%, #9face6 100%);
    border: 0;
    border-radius: 15px;
  }
  </style>
  