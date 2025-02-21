import React from 'react';

function Footer() {
    return (
        <footer style={styles.footer}>
            <p>&copy; {new Date().getFullYear()} Hotpoint Pharmacy. All rights reserved.</p>
            <p>
                <a href="mailto:contact@hotpointpharmacy.com" style={styles.link}>Email Us</a> | 
                <a href="tel:+1234567890" style={styles.link}> Call Us</a>
            </p>
        </footer>
    );
}

const styles = {
    footer: {
        textAlign: 'center',
        padding: '1rem',
        backgroundColor: '#007BFF', // Sky blue shade
        color: 'white',
        position: 'fixed',
        bottom: 0,
        width: '100%',
    },
    link: {
        color: 'white',
        textDecoration: 'none',
        marginLeft: '10px',
    }
};

export default Footer;