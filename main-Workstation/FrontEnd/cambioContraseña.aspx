<%@ Page Language="C#" AutoEventWireup="true" CodeFile="cambioContraseña.aspx.cs" Inherits="_Default" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
        Ingrese su nueva contraseña&nbsp;&nbsp;
        <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>
        <br />
        <br />
        Vuelva a ingresar la nueva contraseña&nbsp;&nbsp;
        <asp:TextBox ID="TextBox2" runat="server"></asp:TextBox>
        <br />
        <br />
        <asp:Button ID="Button1" runat="server" Text="Cambiar Contraseña" />
        <br />
        <br />
        <asp:HyperLink ID="HyperLink2" runat="server" NavigateUrl="~/Index.aspx">Volver a inicio</asp:HyperLink>
        <br />
        <br />
    
    </div>
    </form>
</body>
</html>
