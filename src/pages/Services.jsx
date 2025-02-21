import React from 'react';

function Home() {
    return (
        <div style={styles.container}>
            <h1>Welcome to Hotpoint Pharmacy</h1>
            <p>Your trusted partner for quality pharmaceutical products and healthcare solutions.</p>
            <p>We provide a wide range of medicines, health products, and expert advice to ensure your well-being.</p>
        </div>
    );
}

const styles = {
    container: {
        textAlign: 'center',
        padding: '2rem',
    }
};

export default Home;