<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Site</title>
    <style>
        /* RESET BÁSICO */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
        }

        /* CABEÇALHO */
        header {
            background: #fff;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 0;
        }

        .logo {
            font-size: 24px;
            font-weight: bold;
            color: #1a1a1a;
            text-decoration: none;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 30px;
        }

        nav a {
            text-decoration: none;
            color: #333;
            font-weight: 500;
            transition: color 0.3s;
        }

        nav a:hover {
            color: #007bff;
        }

        /* HERO SECTION */
        .hero {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 150px 0 100px;
            text-align: center;
        }

        .hero h1 {
            font-size: 48px;
            margin-bottom: 20px;
        }

        .hero p {
            font-size: 20px;
            margin-bottom: 30px;
            opacity: 0.9;
        }

        .btn {
            display: inline-block;
            padding: 15px 40px;
            background: #fff;
            color: #667eea;
            text-decoration: none;
            border-radius: 30px;
            font-weight: bold;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }

        /* SEÇÕES */
        section {
            padding: 80px 0;
        }

        .section-title {
            text-align: center;
            font-size: 36px;
            margin-bottom: 50px;
            color: #1a1a1a;
        }

        /* SOBRE */
        .about {
            background: #f9f9f9;
        }

        .about-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            align-items: center;
        }

        .about-text h2 {
            font-size: 28px;
            margin-bottom: 20px;
        }

        .about-image {
            background: #ddd;
            height: 300px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #666;
        }

        /* SERVIÇOS */
        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
        }

        .service-card {
            background: #fff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.3s;
        }

        .service-card:hover {
            transform: translateY(-5px);
        }

        .service-icon {
            font-size: 40px;
            margin-bottom: 20px;
        }

        .service-card h3 {
            margin-bottom: 15px;
            font-size: 20px;
        }

        /* CONTATO */
        .contact {
            background: #1a1a1a;
            color: white;
        }

        .contact .section-title {
            color: white;
        }

        .contact-form {
            max-width: 600px;
            margin: 0 auto;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 15px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
        }

        .form-group textarea {
            height: 150px;
            resize: vertical;
        }

        .btn-submit {
            background: #667eea;
            color: white;
            border: none;
            padding: 15px 40px;
            border-radius: 30px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: background 0.3s;
        }

        .btn-submit:hover {
            background: #764ba2;
        }

        /* RODAPÉ */
        footer {
            background: #111;
            color: #888;
            padding: 30px 0;
            text-align: center;
        }

        /* RESPONSIVO */
        @media (max-width: 768px) {
            .header-content {
                flex-direction: column;
                gap: 15px;
            }

            nav ul {
                gap: 15px;
                font-size: 14px;
            }

            .hero h1 {
                font-size: 32px;
            }

            .about-content {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <!-- CABEÇALHO -->
    <header>
        <div class="container">
            <div class="header-content">
                <a href="#" class="logo">MEU SITE</a>
                <nav>
                    <ul>
                        <li><a href="#inicio">Início</a></li>
                        <li><a href="#sobre">Sobre</a></li>
                        <li><a href="#servicos">Serviços</a></li>
                        <li><a href="#contato">Contato</a></li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>

    <!-- HERO -->
    <section class="hero" id="inicio">
        <div class="container">
            <h1>Bem-vindo ao Meu Site</h1>
            <p>Oferecemos soluções profissionais para seu negócio</p>
            <a href="#contato" class="btn">Fale Conosco</a>
        </div>
    </section>

    <!-- SOBRE -->
    <section class="about" id="sobre">
        <div class="container">
            <h2 class="section-title">Sobre Nós</h2>
            <div class="about-content">
                <div class="about-text">
                    <h2>Quem Somos</h2>
                    <p>Somos uma empresa dedicada a oferecer as melhores soluções para nossos clientes. Com anos de experiência no mercado, notrechos em qualidade e inovação.</p>
                    <br>
                    <p>Nossa missão é transformar ideias em resultados concretos, sempre com transparência e profissionalismo.</p>
                </div>
                <div class="about-image">
                    [COLAR SUA IMAGEM DEPOIS]
                </div>
            </div>
        </div>
    </section>

    <!-- SERVIÇOS -->
    <section id="servicos">
        <div class="container">
            <h2 class="section-title">Nossos Serviços</h2>
            <div class="services-grid">
                <div class="service-card">
                    <div class="service-icon">💼</div>
                    <h3>Consultoria</h3>
                    <p>Especialistas prontos para identificar oportunidades e otimizar seus processos.</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">🎯</div>
                    <h3>Estratégia</h3>
                    <p>Planejamento estratégico para alavancar seu negócio no mercado.</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">⚡</div>
                    <h3>Implementação</h3>
                    <p>Execução rápida e eficiente das soluções planejadas.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CONTATO -->
    <section class="contact" id="contato">
        <div class="container">
            <h2 class="section-title">Fale Conosco</h2>
            <form class="contact-form">
                <div class="form-group">
                    <input type="text" placeholder="Seu Nome" required>
                </div>
                <div class="form-group">
                    <input type="email" placeholder="Seu E-mail" required>
                </div>
                <div class="form-group">
                    <textarea placeholder="Sua Mensagem" required></textarea>
                </div>
                <button type="submit" class="btn-submit">Enviar Mensagem</button>
            </form>
        </div>
    </section>

    <!-- RODAPÉ -->
    <footer>
        <div class="container">
            <p>&copy; 2024 Meu Site. Todos os direitos reservados.</p>
        </div>
    </footer>
</body>
</html>