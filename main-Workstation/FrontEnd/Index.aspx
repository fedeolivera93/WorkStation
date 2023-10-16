<%@ Page Language="C#" AutoEventWireup="true" CodeFile="Index.aspx.cs" Inherits="Index" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
        WorkStation<br />
        <br />
        Ingrese su correo electrónico&nbsp;&nbsp;
        <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>
        <br />
        <br />
        Ingrese su contraseña&nbsp;&nbsp;
        <asp:TextBox ID="TextBox2" runat="server"></asp:TextBox>
        <br />
        <br />
        <asp:Button ID="Button1" runat="server" Text="Iniciar Sesión" />
        <br />
        <br />
        ¿Olvidó su contraseña? <asp:HyperLink ID="HyperLink1" runat="server" NavigateUrl="~/Recuperar.aspx">Click aquí</asp:HyperLink>
&nbsp;para recuperarla.</div>
    </form>
</body>
</html>
