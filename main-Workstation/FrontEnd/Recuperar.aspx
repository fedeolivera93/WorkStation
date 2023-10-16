<%@ Page Language="C#" AutoEventWireup="true" CodeFile="Recuperar.aspx.cs" Inherits="Recuperar" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
        Recuperación de Contraseña<br />
        <br />
        Ingrese su correo electrónico:&nbsp;&nbsp;
        <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>
        <br />
        <br />
        Ingrese su token:&nbsp;&nbsp;
        <asp:TextBox ID="TextBox2" runat="server"></asp:TextBox>
        <br />
        <br />
        <asp:Button ID="Button1" runat="server" Text="Recuperar Contraseña" />
        <br />
        <br />
        <asp:HyperLink ID="HyperLink1" runat="server" NavigateUrl="~/Index.aspx">Volver</asp:HyperLink>
    
    </div>
    </form>
</body>
</html>
